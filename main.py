# The command for the bot is *m or *toggle_mute_all
# You have to place your private api key for the TOKEN variable!
# The channel of a member only updates when they leave or join so if
# you started the bot while you're in a channel it won't detect you


import discord
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

client = commands.Bot(command_prefix='*')
TOKEN = 'PRIVATE-API-KEY' # PLACE YOUR API KEY HERE
toggle = True

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb)
    print('Bot is ready.')


@has_permissions(administrator=True)
@client.command(aliases=['m'])
async def toggle_mute_all(ctx):
    global toggle
    channel = ctx.author.voice.channel
    members = channel.members
    for i in range(len(members)):
        await members[i].edit(mute=toggle)

    if toggle:
        toggle = False
        return;
    toggle = True


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command")
    else:
        print(error)

