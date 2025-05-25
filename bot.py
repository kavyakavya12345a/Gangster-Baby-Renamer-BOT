import asyncio
from pyrogram import Client, idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
STRING = os.environ.get("STRING", "")

bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

async def start_all():
    if STRING:
        apps = [Client2, bot]

        # Clock sync ke liye chhoti delay
        await asyncio.sleep(2)

        for app in apps:
            await app.start()
        
        await idle()

        for app in apps:
            await app.stop()

    else:
        await bot.start()
        await idle()
        await bot.stop()

if name == "main":
    asyncio.run(start_all())
