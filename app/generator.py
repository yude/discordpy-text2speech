from os import remove
import subprocess
import re

# Supress to speech containing custom emojis
def remove_custom_emoji(text):
    pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>'
    return re.sub(pattern, '', text)

# Skip URLs
def remove_urls(text):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern, 'URL省略', text)

# Push messages into text files
def WAV(input):
    input = remove_custom_emoji(input)
    input = remove_urls(input)
    input_file = '/app/data/input.txt'
    
    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(input)
    
    command = '/usr/local/bin/open_jtalk -x {x} -m {m} -r {r} -ow {ow} {input_file}'
    # Path to dictionary
    x = '/usr/local/lib/open_jtalk_dic_utf_8-1.09'
    # Path to htsvoice
    m = '/usr/local/lib/hts_voice_nitech_jp_atr503_m001-1.05/nitech_jp_atr503_m001.htsvoice'
    r = '1.0' # Speaking speed
    ow = '/app/data/output.wav' # Path to output file
    # Set command arguments
    args= {'x': x, 'm': m, 'r': r, 'ow': ow, 'input_file': input_file}
    
    # Run the command
    cmd = command.format(**args)
    print(cmd)
    subprocess.run(cmd, shell=True)
    
    return True

if __name__ == '__main__':
    WAV('テスト')
