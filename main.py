import os
from random import randint

from ossapi import Ossapi
from dotenv import load_dotenv
from typing import Final
import discord
from discord import Message, Client
from ossapi import Ossapi, Scope

role_id = 1219949517374361600
verify_channel = "verif"

load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CLIENT_ID: Final[str] = os.getenv('CLIENT_ID')
CLIENT_SECRET: Final[str] = os.getenv('CLIENT_SECRET')

scopes = [Scope.PUBLIC, Scope.CHAT_WRITE]

callback_url = "http://localhost:4242/"

api = Ossapi(CLIENT_ID, CLIENT_SECRET, redirect_uri=callback_url, scopes=scopes)

intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running')
    print(f'Latency: {client.latency}')

@client.event
async def on_message(message: Message) -> None:

    username: str = str(message.author)
    user_message: str = message.content

    if message.author == client.user or message.author.bot:
        return

    elif read_verified(message.author):
        await message.add_reaction("✅")
        role = message.guild.get_role(role_id)
        await message.author.add_roles(role)
        print(f"{message.author} is already verified.")

    channel: str = str(message.channel)
    server = message.guild
    server_name = server.name if server else None

    if str(message.channel) == verify_channel:
        if user_message[0:7] == "!verify":
            if len(user_message) <= 10 :
                await message.reply("Please provide an osu username.")
                return
            
            nickname = user_message[8:]
            nickname_id = api.user(nickname).id
            nickname_ig = api.user(nickname_id).username

            code = generate_code(username, nickname_ig)

            api.send_pm(nickname_id, f"Your verification code for {server_name} is {code}")
            await message.reply(f"A verification code has been sent to {nickname_ig} on osu.")
            
            if read_list(username) is False:
                add_to_list(username)
            if read_verified(username) is False:
                add_to_verified(username)

        elif user_message.isdigit() :
            valid = read_code(username, user_message)
            if valid[0]:
                await message.add_reaction("✅")
                role = message.guild.get_role(role_id)
                await message.author.add_roles(role)
                add_to_verified(message.author)
                print(f"{message.author} has been verified.")
            else:
                await message.add_reaction("❌")
        elif user_message[0] == "!":
            await message.reply("!verify ``osu username``")
        return

def add_to_list(username_discord):
    with open(os.path.join("players", "_list.log"), 'a', encoding='utf-8') as file:
        file.write(f"{username_discord} ")

def add_to_verified(username_discord):
    with open(os.path.join("players", "_verified.log"), 'a', encoding='utf-8') as file:
        file.write(f"{username_discord} ")

def generate_code(username_discord, username_ig):
    code = '{:06d}'.format(randint(0, 999999))
    with open(os.path.join("players", f"{username_discord}.log"), 'w', encoding='utf-8') as file:
        file.write(f"{username_ig} {code}")
    return code

def read_code(username_discord, confirmation_code):
    with open(os.path.join("players", f"{username_discord}.log")) as file:
        a = file.read().split(" ")
    if a[1] == confirmation_code :
        return (True, a[0])
    return (False, a[0])

def read_list(username):
    with open(os.path.join("players", "_list.log")) as file:
        a = file.read().split(" ")
    if username in a:
        return True
    return False

def read_verified(username):
    with open(os.path.join("players", "_verified.log")) as file:
        a = file.read().split(" ")
    if username in a:
        return True
    return False 

def main() -> None:
    client.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()

