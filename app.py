import os

import discord
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()

client.run(os.getenv("TOKEN"))
