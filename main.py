import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


PREFIX = "?"


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=PREFIX, intents=intents)
    @bot.event
    async def on_ready():
        print("Bot hazır.")
        await bot.load_extension("bot")
    load_dotenv()
    if os.environ["BOT_TOKEN"]=="":
        print("Lütfen bot tokeninizi .env dosyasına giriniz!")
        exit()
    bot.run(os.environ["BOT_TOKEN"])

if __name__ == "__main__":
    run()
