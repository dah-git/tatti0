import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram
from tobrot import AUTH_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    await message.reply_text("Hi ! 👇 Click Here To Help", 
                             reply_markup=InlineKeyboardMarkup(
                                                               [
                                                                  [
                                                                   InlineKeyboardButton("Click Me", url=f"https://telegra.ph/file/dad6b09bbf533be743fce.jpg")
                                                                  ]
                                                               ]
                            ), disable_web_page_preview=True, parse_mode="markdown")

