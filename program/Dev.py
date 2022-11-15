import asyncio

from sys import version_info
from program import __version__
from driver.veez import user
from config import SUDO_USERS
from driver.filters import command, other_filters
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

SUDO_USERS = getenv("SUDO_USERS")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@Client.on_message(command(["مطور البوت", "المطور", "مطور"]))
async def muamen(client: Client, message: Message):
  usrr = await client.get_users(SUDO_USERS)
  userr = await client.get_chat(SUDO_USERS)
  shad = usrr.first_name
  namee = usrr.mention
  uuser = usrr.username
  Bioo = userr.bio
  async for photo in client.iter_profile_photos(SUDO_USERS, limit=1):
           await message.reply_photo(photo.file_id,       caption=f"""❲ **Developer Bot** ❳\n— — — — — — — — —\n𖥔 **Dev Name :** {namee}\n𖥔 **Dev User :** @{uuser}\n𖥔 **Dev Id :** {SUDO_USERS}\n𖥔 **Dev Bio :**{Bioo}""",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    shad, url=f"https://t.me/{uuser}"
            ),
            ],
            [
                InlineKeyboardButton(
                   "ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/S88DBOT?startgroup=true"
                ),
            ],
        ]
      )
    )
