import asyncio

from sys import version_info
from program import __version__
from driver.veez import user
from config import OWNER_ID
from driver.filters import command, other_filters
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest


@Client.on_message(command(["مطور السورس", "مبرمج السورس", "مؤمن", "شادو"]))
async def muamen(client: Client, message: Message):
  usr = await client.get_users("1970797144")
  user = await client.get_chat("1970797144")
  shad = usr.first_name
  useer = usr.username
  Bio = user.bio
    await message.reply_photo(
        photo=f"https://t.me/S550D",
        caption=f"""**▷ ᴅᴇᴠ sᴏᴜʀᴄᴇ ʟụɴᴀ ѕʜᴀᴅᴏᴡ ♯**\n**▷ɴᴀᴍᴇ ѕʜᴀᴅᴏᴡ ⇿** {shad}\n**▷ ɪᴅ ѕʜᴀᴅᴏᴡ ⇿** 1970797144\n**▷ ʙɪᴏ ѕʜᴀᴅᴏᴡ ⇿** {Bio}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("♢ ѕᴏụʀᴄᴇ ♢", url=f"https://t.me/FA9SH"),
                    InlineKeyboardButton("♢ ʙᴏᴛ ʟụɴᴀ ♢", url=f"https://t.me/S88DBOT")
                ],
                [
                    InlineKeyboardButton(
                        shad, url=f"https://t.me/{useer}"
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
