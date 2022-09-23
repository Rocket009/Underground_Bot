import discord
from private.config import Token


class Client(discord.Client):

    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)


    async def on_ready(self):
        print("We have logged in as {0}".format(self.user))


def main():
    client = Client()
    client.run(Token)

if __name__ == "__main__":
    main()