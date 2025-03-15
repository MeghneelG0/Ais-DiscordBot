import discord
from discord.ext import commands
from config import TOKEN, intents

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')
    CHANNEL_ID = 1344913738255433761
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("Hello! I'm online and ready to work. 🚀")
    else:
        print("❌ Error: Channel not found. Check the ID.")

# Load cogs
bot.load_extension('cogs.test')

bot.run(TOKEN)