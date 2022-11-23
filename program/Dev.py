import asyncio

from sys import version_info
from program import __version__
from driver.veez import user
from config import SUDO_USERS, ASSISTANT_NAME, BOT_TOKEN 
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

BOT_TOKEN = getenv("BOT_TOKEN")

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


@Client.on_message(command(["مطور السورس", "مبرمج السورس", "مؤمن", "شادو"]) & ~filters.edited)
async def shadow(client: Client, message: Message):
  usr = await client.get_users("1970797144")
  user = await client.get_chat("1970797144")
  shad = usr.first_name
  mua = usr.mention
  useer = usr.username
  Bio = user.bio
  async for photo in client.iter_profile_photos("1970797144", limit=1):
           await message.reply_photo(photo.file_id,       caption=f"""**▷ ᴅᴇᴠ sᴏᴜʀᴄᴇ ʟụɴᴀ ѕʜᴀᴅᴏᴡ ♯**\n**▷ɴᴀᴍᴇ ѕʜᴀᴅᴏᴡ ⇿** {mua}\n**▷ ɪᴅ ѕʜᴀᴅᴏᴡ ⇿** 1970797144\n**▷ ʙɪᴏ ѕʜᴀᴅᴏᴡ ⇿** {Bio}""",
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


@Client.on_message(command(["مطور البوت", "المطور", "مطور"]) & ~filters.edited)
async def dev(client: Client, message: Message):
  dusr = await client.get_users(SUDO_USERS)
  duser = await client.get_chat(SUDO_USERS)
  shad = dusr.first_name
  namee = dusr.mention
  uuser = dusr.username
  Bioo = duser.bio
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


@Client.on_message(command(["المساعد", "الحساب المساعد"]) & ~filters.edited)
async def muamen(client: Client, message: Message):
  ausr = await client.get_users(BOT_TOKEN)
  aname = ausr.first_name
  anamee = ausr.mention
  auser = ausr.username
  async for photo in client.iter_profile_photos(BOT_TOKEN, limit=1):
           await message.reply_photo(photo.file_id,       caption=f"""🦅 الحساب المساعد الخاص بالبوت:\n{anamee}\n√""",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    aname, url=f"https://t.me/{auser}"
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


@Client.on_message(command(["السورس", "سورس"]) & ~filters.edited)
async def source(client: Client, message: Message):
  sousr = await client.get_users("1970797144")
  sohad = sousr.first_name
  souser = sousr.username
  await message.reply_text(
        f"""
╭──── • ◈ • ────╮\n么 [𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗘𝗚𝗔](t.me/FA9SH)\n么 [𝗔𝗦𝗞 𝗧𝗢 𝗠𝗘](t.me/S88DBOT)\n么 [𝑺𝑯𝑨𝑫𝑶𝑾](t.me/S550D)\n╰──── • ◈ • ────╯\n⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        sohad, url=f"https://t.me/{souser}"
                ),
                ],
                [
                    InlineKeyboardButton(
                       "CH SOURCE", url=f"https://t.me/FA9SH"
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
