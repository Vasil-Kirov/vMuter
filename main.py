from discord import *
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix='#')
TOKEN = 'NzY1NjQ5NjcxMjA4MDQyNTI4.X4X40g.LZ_vRyK5_oYs2hOeG02rmao9ABQ'


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb)
    print('Bot is ready.')


@client.command(aliases=['tmall'])
async def toggle_mute_all(ctx):
    guild=ctx.message.guild




client.run(TOKEN)
