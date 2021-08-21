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
    
    cmd = ("./convert.sh")
    print(cmd)
    subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    
    return True

if __name__ == '__main__':
    WAV('テスト')
