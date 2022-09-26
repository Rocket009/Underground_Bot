import discord
from discord import app_commands
from private.config import DiscordToken
from Commands import callbacks


class Client(discord.Client):

    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)


    async def on_ready(self):
        print("We have logged in as {0}".format(self.user))
        await tree.sync(guild=discord.Object(id=1018192683723915284))



def main():
    client = Client()
    global tree
    tree = app_commands.CommandTree(client)
    callbacks(tree)

    client.run(DiscordToken)

if __name__ == "__main__":
    main()

