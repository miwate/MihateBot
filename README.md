# MihateBot
Discord bot that gives a role after a verification code sent on osu.

# Setup
This program uses the python wrapper for osu! [Ossapi](https://tybug.github.io/ossapi/)

## API and OAuth
- Create a new OAuth Application on your [osu! settings](https://osu.ppy.sh/home/account/edit).
  Application callback URL is set to ```http://localhost:4242``` as an example.

In the ```.env``` file, paste your :
- Discord application token after ```DISCORD_TOKEN=```. You can create one on the [Developper portal](https://discord.com/developers/applications) page
- osu! OAuth secret id after the ```CLIENT_ID```
- osu! OAuth secret client after the ```CLIENT_SECRET```

## Discord
In the ```main.py``` file, paste your :
- Discord role id after the ```role_id```
- Discord text channel name after the ```verify_channel```

## Dependencies
In your terminal, install the following dependencies using [pip](https://pypi.org/project/pip/).
- [discord](https://pypi.org/project/discord.py/)
- [typing](https://pypi.org/project/typing/)
- [ossapi](https://pypi.org/project/ossapi/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
