import discord
from discord.ext import commands
from tokenbot import bottoken

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Привет! Я бот который поможет разщитать электропотребление твоего дома/квартиры.")
    await ctx.send("Напиши $start чтобы начать.")
#f
@bot.command()
async def start(ctx):
    await ctx.send("1. У вас дом или квартира?")
    await ctx.send("Если дом то напишите $ff")
    await ctx.send("Если квартира то напишите $fs")
#s
@bot.command()
async def ff(ctx):
    house = True
    await ctx.send("2. Размер вашего дома?")
    await ctx.send("Если маленький то напишите $sff")
    await ctx.send("Если средний то напишите $sfs")
    await ctx.send("Если большой то напишите $sft")

@bot.command()
async def fs(ctx):
    house = False
    await ctx.send("2. Размер вашей квартиры?")
    await ctx.send("Если маленькая то напишите $ssf")
    await ctx.send("Если средняя то напишите $sss")
    await ctx.send("Если большая то напишите $sst")
#t
@bot.command()
async def sff(ctx):
    await ctx.send("3. Кол-во больших приборов?")
    await ctx.send("Если меньше 5 то напишите $tfff")
    await ctx.send("Если от 5 до 10 то напишите $tffs")
    await ctx.send("Если больше 10 то напишите $tfft")

@bot.command()
async def sfs(ctx):
    await ctx.send("3. Кол-во больших приборов?")
    await ctx.send("Если меньше 5 то напишите $tfsf")
    await ctx.send("Если от 5 до 10 то напишите $tfss")
    await ctx.send("Если больше 10 то напишите $tfst")

@bot.command()
async def sft(ctx):
    await ctx.send("3. Кол-во больших приборов?")
    await ctx.send("Если меньше 5 то напишите $tftf")
    await ctx.send("Если от 5 до 10 то напишите $tfts")
    await ctx.send("Если больше 10 то напишите $tftt")

@bot.command()
async def ssf(ctx):
    await ctx.send("3. Кол-во больших приборов?")
    await ctx.send("Если меньше 5 то напишите $tsff")
    await ctx.send("Если от 5 до 10 то напишите $tsfs")
    await ctx.send("Если больше 10 то напишите $tsft")

@bot.command()
async def sss(ctx):
    await ctx.send("3. Кол-во больших приборов?")
    await ctx.send("Если меньше 5 то напишите $tssf")
    await ctx.send("Если от 5 до 10 то напишите $tsss")
    await ctx.send("Если больше 10 то напишите $tsst")

@bot.command()
async def sst(ctx):
    await ctx.send("3. Кол-во больших приборов?")
    await ctx.send("Если меньше 5 то напишите $tstf")
    await ctx.send("Если от 5 до 10 то напишите $tsts")
    await ctx.send("Если больше 10 то напишите $tstt")

#хороший результат

@bot.command()
async def tfff(ctx):
    await ctx.send("У вас хороший результат!")

@bot.command()
async def tfsf(ctx):
    await ctx.send("У вас хороший результат!")

@bot.command()
async def tfss(ctx):
    await ctx.send("У вас хороший результат!")
@bot.command()
async def tftf(ctx):
    await ctx.send("У вас хороший результат!")

@bot.command()
async def tfts(ctx):
    await ctx.send("У вас хороший результат!")

@bot.command()
async def tftt(ctx):
    await ctx.send("У вас хороший результат!")

@bot.command()
async def tssf(ctx):
    await ctx.send("У вас хороший результат!")

@bot.command()
async def tstf(ctx):
    await ctx.send("У вас хороший результат!")

#средний результат

@bot.command()
async def tffs(ctx):
    await ctx.send("У вас средний результат!")

@bot.command()
async def tfst(ctx):
    await ctx.send("У вас средний результат!")

@bot.command()
async def tsff(ctx):
    await ctx.send("У вас средний результат!")

@bot.command()
async def tsss(ctx):
    await ctx.send("У вас средний результат!")

@bot.command()
async def tsts(ctx):
    await ctx.send("У вас средний результат!")

@bot.command()
async def tstt(ctx):
    await ctx.send("У вас средний результат!")

#плохой результат

@bot.command()
async def tfft(ctx):
    await ctx.send("У вас плохой результат!")

@bot.command()
async def tsft(ctx):
    await ctx.send("У вас плохой результат!")

@bot.command()
async def tsst(ctx):
    await ctx.send("У вас плохой результат!")




bot.run(bottoken)
