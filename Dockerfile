FROM python:3.8.11-alpine3.13
ADD ./app /app

# Set working directory
WORKDIR /app

# Install dependencies
RUN apk --update add libffi-dev gcc make g++
RUN pip install -r requirements.txt

# Run bot
CMD ["python", "bot.py"]
