from discord.ext import commands
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="da#", intents=intents)
token = input("Token: ")

da = [
    "https://cdn.discordapp.com/embed/avatars/0.png",
    "https://cdn.discordapp.com/embed/avatars/1.png",
    "https://cdn.discordapp.com/embed/avatars/2.png",
    "https://cdn.discordapp.com/embed/avatars/3.png",
    "https://cdn.discordapp.com/embed/avatars/4.png",
    "https://cdn.discordapp.com/embed/avatars/5.png"
]

@bot.event
async def on_ready():
    print("on ready!")

@bot.command()
async def list(ctx):
    u = []
    for member in ctx.guild.members:
        if str(member.avatar_url) in da:
            print(f"{member.name}#{member.discriminator} True")
            u.append(member.mention)
        else:
            print("false")
    ul = "\n".join(u)
    embed = discord.Embed(title="Default Avatarのリスト:", description=ul, color=discord.Colour.random())
    await ctx.send(embed=embed)


bot.run(token)
