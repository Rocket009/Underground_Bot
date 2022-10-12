import discord
from discord import Team, app_commands
from cfb import cfb_api
import footy 


def callbacks(tree : app_commands.CommandTree):
    cfb_obj = cfb_api()
    foot_obj=footy.footydb()

    @tree.command(name = "echo", description = "echo text", guild = discord.Object(id=1018192683723915284))
    async def self(interaction: discord.Interaction, name : str):
        await interaction.response.send_message(name)

    @tree.command(name = "test", description="prints your name", guild = discord.Object(id=1018192683723915284))
    async def self(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")

    @tree.command(name = "cfb_rank", description="Prints the current CFB rankings", guild = discord.Object(id=1018192683723915284))
    async def self(interaction : discord.Interaction):
        r = cfb_obj.get_rankings()
        index = 0
        for schools in r:
            await interaction.channel.send(f"Rank #{index + 1} {schools}")
            index += 1

    @tree.command(name = "PL_table", description="Prints the current English Premier League table", guild = discord.Object(id=1018192683723915284))
    async def self(interaction : discord.Interaction):
        table = foot_obj.get_table()
        for team in table:
            await interaction.channel.send(f"{team}")