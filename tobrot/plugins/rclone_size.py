import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
import subprocess
import os
import asyncio
import re
from tobrot import (
    EDIT_SLEEP_TIME_OUT,
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def g_clearme(client, message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton("Yes 🚫", callback_data=("fuckingdo").encode("UTF-8")))
    ikeyboard.append(InlineKeyboardButton("No 🤗", callback_data=("fuckoff").encode("UTF-8")))
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text("Are you sure? 🚫 This will delete all your downloads locally 🚫", reply_markup=reply_markup, quote=True)
