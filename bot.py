import discord
import ollama
from discord.ext import commands
from config import TOKEN, intents

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')
    CHANNEL_ID = 1344913738255433761
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("Hello! I'm online and ready to work. 🚀")
    else:
        print("❌ Error: Channel not found. Check the ID.")


@bot.command(name="ask")
async def ask(ctx, *, question: str):
    """Ask the LLM a question and send the response to Discord."""
    try:
        # Query the LLM using Ollama
        response = ollama.chat(
            model="llama3.2",  # Replace with the name of your model
            messages=[{"role": "user", "content": question}]
        )

        # Extract the LLM's response
        llm_response = response["message"]["content"]

        # Send the response back to Discord
        await ctx.send(llm_response)
    except Exception as e:
        await ctx.send(f"Error querying the LLM: {e}")

# Load cogs
bot.load_extension('cogs.test')

bot.run(TOKEN)