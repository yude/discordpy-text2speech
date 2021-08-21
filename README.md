# discord-text2speech
👄 Discord simple text-to-speech Bot

## Docker Compose
Create `docker-compose.yml` and paste below, then set `TOKEN` variable, and finally run `docker-compose up -d`.
```
version: '3'
services:
  discord-text2speech:
    restart: always
    container_name: discord-text2speech
    image: yude/discord-text2speech
    environment:
      # Discord bot token
      - TOKEN=
```

## License
### discord-text2speech
This repository is licensed under the MIT License.
### [open_jtalk-docker](https://github.com/u6k/open_jtalk-docker)
It's lead by [u6k](https://github.com/u6k), and discord-text2speech uses it partially.\
open_jtalk-docker is also licensed under the MIT License.
