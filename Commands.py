import discord
from discord import app_commands
from cfb import cfb_api

GUILDS = [discord.Object(id=1018192683723915284), discord.Object(id=913064913113587712)]

def callbacks(tree : app_commands.CommandTree):
    cfb_obj = cfb_api()

    @tree.command(name = "echo", description = "echo text", guilds=GUILDS)
    async def self(interaction: discord.Interaction, name : str):
        await interaction.response.send_message(name)

    @tree.command(name = "test", description="prints your name", guilds=GUILDS)
    async def self(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")

    @tree.command(name = "cfb_rank", description="Prints the current AP Top 25 CFB rankings", guilds=GUILDS)
    async def self(interaction : discord.Interaction):
        await interaction.response.send_message("The ranks are\n")
        r = cfb_obj.get_rankings()
        index = 0
        for schools in r:
            await interaction.channel.send(f"Rank #{index + 1} {schools}")
            index += 1

    @tree.command(name = "cfb_rank_no", description="Prints the current AP Top 25 CFB rankings based on the number given", guilds=GUILDS)
    async def self(interaction : discord.Interaction, number : str):
        await interaction.response.send_message("The ranks are\n")
        r = cfb_obj.get_rankings()
        index = 0
        for schools in r:
            if index + 1 > int(number):
                break 
            await interaction.channel.send(f"Rank #{index + 1} {schools}")
            index += 1

    @tree.command(name="cfb_good_games", description="Prints all of the ranked vs ranked games for the upcoming week", guilds=GUILDS)
    async def self(interaction : discord.Interaction):
        await interaction.response.send_message("The good games this week are\n")
        games = cfb_obj.getgoodgames()
        for game in games:
            await interaction.channel.send(game)

    @tree.command(name="game_search", description="Prints the opponite for the game this week", guilds=GUILDS)
    async def self(interaction : discord.Interaction, team : str):
        await interaction.response.send_message(cfb_obj.searchgame(team))