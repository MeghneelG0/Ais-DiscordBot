import os
from dotenv import load_dotenv

# Load .env file to keep token secure
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    raise ValueError("No DISCORD_BOT_TOKEN found in environment variables")

# Define intents (Mandatory for modern bots)
import discord
intents = discord.Intents.default()
intents.message_content = True  # Enable message events
intents.guilds = True