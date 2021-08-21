FROM ubuntu:latest

# Load source files
ADD ./app /app

# Install dependencies
RUN apt -y update; apt -y upgrade; apt -y install libffi-dev wget git build-essential
RUN pip install -r requirements.txt

# Setup Open JTalk
## Special thanks to u6k: https://github.com/u6k/open_jtalk-docker
WORKDIR /usr/local/src/

RUN wget http://downloads.sourceforge.net/hts-engine/hts_engine_API-1.10.tar.gz && \
    tar zxvf hts_engine_API-1.10.tar.gz && \
    cd hts_engine_API-1.10/ && \
    ./configure && \
    make && \
    make install

COPY manobi.patch manobi.patch

RUN wget http://downloads.sourceforge.net/open-jtalk/open_jtalk-1.09.tar.gz && \
    tar zxvf open_jtalk-1.09.tar.gz && \
    cd open_jtalk-1.09/ && \
    patch -p0 < /usr/local/src/manobi.patch && \
    ./configure --with-hts-engine-header-path=/usr/local/include --with-hts-engine-library-path=/usr/local/lib --with-charset=UTF-8 && \
    make && \
    make install

RUN wget http://downloads.sourceforge.net/open-jtalk/hts_voice_nitech_jp_atr503_m001-1.05.tar.gz && \
    tar zxvf hts_voice_nitech_jp_atr503_m001-1.05.tar.gz && \
    cp -r hts_voice_nitech_jp_atr503_m001-1.05 /usr/local/lib/hts_voice_nitech_jp_atr503_m001-1.05

RUN wget http://downloads.sourceforge.net/open-jtalk/open_jtalk_dic_utf_8-1.09.tar.gz && \
    tar zxvf open_jtalk_dic_utf_8-1.09.tar.gz && \
    cp -r open_jtalk_dic_utf_8-1.09 /usr/local/lib/open_jtalk_dic_utf_8-1.09

# Set working directory
WORKDIR /app

# Run bot
CMD ["python", "bot.py"]
