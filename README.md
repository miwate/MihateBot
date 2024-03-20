# MihateBot
Discord bot that gives a role after a verification code sent on osu.

## Setup
This program uses the python wrapper for osu! [Ossapi](https://tybug.github.io/ossapi/)

# API and OAuth
- Create a new OAuth Application on your [osu! settings](https://osu.ppy.sh/home/account/edit).
  Application callback URL is set to ```bash http://localhost:4242``` as an example.

In the ```bash .env``` file, paste your :
- Discord application token after ```bash DISCORD_TOKEN=```. You can create one on the [Developper portal](https://discord.com/developers/applications) page
- osu! OAuth secret id after the ```bash CLIENT_ID```
- osu! OAuth secret client after the ```bash CLIENT_SECRET```

In the ```main.py``` file, paste your :
