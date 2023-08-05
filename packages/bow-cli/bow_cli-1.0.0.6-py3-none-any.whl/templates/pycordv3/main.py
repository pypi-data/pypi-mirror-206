import pycord

bot = pycord.Bot(pycord.Intents())


@bot.listen(pycord.Ready)
async def on_ready() -> None:
    print('Bot is ready!')


@bot.command()
async def hello(ctx: pycord.Context) -> None:
    await ctx.send('Hello :wave:!')


# REMEMBER TO CHANGE THIS!
bot.run("TOKEN")