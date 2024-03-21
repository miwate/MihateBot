# MihateBot
### Discord bot that gives a role after a verification code sent on osu.
If you think the project can be improved (which is the case), do not hesitate to open pull requests and contact me on discord @mihate.
This program uses the python wrapper for osu! [Ossapi](https://tybug.github.io/ossapi/)

# How to run it yourself

## API and OAuth
- Create a new OAuth Application on your [osu! settings](https://osu.ppy.sh/home/account/edit).
  Application callback URL is set to ```http://localhost:4242``` as an example.

In the ```.env``` file, paste your :
- Discord application token after ```DISCORD_TOKEN```. You can create one on the [Developper portal](https://discord.com/developers/applications) page
- osu! OAuth secret id after the ```CLIENT_ID```
- osu! OAuth secret client after the ```CLIENT_SECRET```

## Discord
In the ```main.py``` file, paste your :
- Discord role id after the ```role_id```
- Discord text channel name after the ```verify_channel```, default is set to ```verif```

## Dependencies
In your terminal, install the following dependencies using [pip](https://pypi.org/project/pip/).
- [discord](https://pypi.org/project/discord.py/)
- [typing](https://pypi.org/project/typing/)
- [ossapi](https://pypi.org/project/ossapi/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

# How to use it
In a channel named ```verif``` (default value for ```verify_channel```), type ```!verify foobar``` (replace foobar with your actual osu! username, example ```!verify Hardstuck 2```).
For the first execution, ossapi will need a confirmation by hand to get access to your osu account (PUBLIC and CHAT_WRITE) to be able to send private messages.
A 6-digit code will be sent to the specified osu! account by using your osu! account.
Then, send the 6-digit in the discord verification channel. MihateBot will give you the specified role ```role_id```.
The bot needs to read the channel ```verify_channel``` only.
