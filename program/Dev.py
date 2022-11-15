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


@Client.on_message(command(["مطور السورس", "مبرمج السورس", "مؤمن", "شادو"]))
async def shadow(client: Client, message: Message):
  usr = await client.get_users("1970797144")
  user = await client.get_chat("1970797144")
  shad = usr.first_name
  mua = usr.mention
  useer = usr.username
  Bio = user.bio
  await message.reply_photo(
    photo=f"https://t.me/S550D",
    caption=f"""**▷ ᴅᴇᴠ sᴏᴜʀᴄᴇ ʟụɴᴀ ѕʜᴀᴅᴏᴡ ♯**\n**▷ɴᴀᴍᴇ ѕʜᴀᴅᴏᴡ ⇿** {mua}\n**▷ ɪᴅ ѕʜᴀᴅᴏᴡ ⇿** 1970797144\n**▷ ʙɪᴏ ѕʜᴀᴅᴏᴡ ⇿** {Bio}""",
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


@Client.on_message(command(["مطور البوت", "المطور", "مطور"]))
async def muamen(client: Client, message: Message):
  usr = await client.get_users(SUDO_USERS)
  user = await client.get_chat(SUDO_USERS)
  shadow = usr.first_name
  namee = usr.mention
  uuser = usr.username
  Bioo = user.bio
  await message.reply_photo(
    photo=f"https://t.me/S550D",
    caption=f"""❲ **Developer Bot** ❳\n— — — — — — — — —\n𖥔 **Dev Name :** {namee}\n𖥔 **Dev User :** @{uuser}\n𖥔 **Dev Id :** {SUDO_USERS}\n𖥔 **Dev Bio :**{Bioo}""",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    shadow, url=f"https://t.me/{uuser}"
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
