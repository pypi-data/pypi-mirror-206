import discord

bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.slash_command()
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello :wave:!")


# REMEMBER TO CHANGE THIS!
bot.run("TOKEN")