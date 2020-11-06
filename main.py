import discord
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from time import time
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

client = commands.Bot(command_prefix='*')
TOKEN = 'NzY1NjQ5NjcxMjA4MDQyNTI4.X4X40g.LZ_vRyK5_oYs2hOeG02rmao9ABQ'
to_be_unmuted = []
left_time = []
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
    else:
        toggle = True


@client.event
async def on_voice_state_update(member, before, after):
    global to_be_unmuted
    global left_time
    try:
        if before.channel is not None and after.channel is None and member not in to_be_unmuted:
            to_be_unmuted.append(member)
            left_time.append(time())

        elif before.channel is None and after.channel is not None and member in to_be_unmuted and left_time[to_be_unmuted.index(member)] - time() < -500:
            await member.edit(mute=False)
            del left_time[to_be_unmuted.index(member)]
            to_be_unmuted.remove(member)
        else:
            print("Time left: ", left_time[to_be_unmuted.index(member)] - time() + 500)
    except ValueError:
        pass


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command")
    else:
        print(error)


# print(ctx.author.voice.channel.id)

# 765279669024325646


client.run(TOKEN)
