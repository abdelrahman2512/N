import asyncio

from datetime import datetime
from sys import version_info
from time import time
from driver.veez import user as USER
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from driver.decorators import sudo_users_only
from config import SUDO_USERS, BOT_USERNAME, SUBSCRIBE, FORCE_SUBSCRIBE_TEXT, UPDATES_CHANNEL
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup, ChatJoinRequest

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)

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

@Client.on_message(
    command(["/start", f"/start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    if SUBSCRIBE == "y":
        try:
           statusch = await client.get_chat_member(f"@{UPDATES_CHANNEL}", message.from_user.id)
           if not statusch.status:
              await message.reply_text(
              text=FORCE_SUBSCRIBE_TEXT,
              reply_markup=InlineKeyboardMarkup(
                  [[InlineKeyboardButton(text="اشترك في قناة البوت", 
                  url=f"https://telegram.me/{UPDATES_CHANNEL}")]]
            )
         )
              return
        except Exception as error:
            await message.reply_text(
            text=FORCE_SUBSCRIBE_TEXT,
            reply_markup=InlineKeyboardMarkup(
                  [[InlineKeyboardButton(text="اشترك في قناة البوت", 
                  url=f"https://telegram.me/{UPDATES_CHANNEL}")]]
            )
         )
            return
    if message.from_user.id in SUDO_USERS:
       await message.reply_text(
                "💌╖اهلا بيك حبيبي آلمـطـور\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس [دوس هنا](https://t.me/FA9SH)",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["مبرمج السورس"],
                        ["السورس","المطور"],
                        ["الحساب المساعد"],
                        ["الغاء"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
        try:
           await message.reply_photo(
           photo=f"https://t.me/S550D",
           caption=f"""ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\n🎤╖ أهلآ بك عزيزي أنا بوت شادو\n⚙️╢ وظيفتي حماية المجموعات\n✅╢ لتفعيل البوت عليك اتباع مايلي\n🔘╢ أضِف البوت إلى مجموعتك\n⚡️╢ ارفعهُ » مشرف\n⬆️╜ سيتم ترقيتك مالك في البوت\nـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("الاوامر 📚", callback_data="cbcmds"),
                    InlineKeyboardButton("ℹ️ حول", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton("تغير اللغه 🌐", callback_data="lang"),
                ],
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
    )



@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply_photo(
              photo=f"https://telegra.ph/file/751389a9543aec27b59e8.jpg",
              caption=f"""ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\n🎤╖ أهلآ بك عزيزي أنا بوت شادو\n⚙️╢ وظيفتي حماية المجموعات\n✅╢ لتفعيل البوت عليك اتباع مايلي\n🔘╢ أضِف البوت إلى مجموعتك\n⚡️╢ ارفعهُ » مشرف\n⬆️╜ سيتم ترقيتك مالك في البوت\nـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅",
                        url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"👮🏼 (> {suspect} <)\n\n**Gbanned** user detected, that user has been gbanned by sudo user and was blocked from this Chat !\n\n🚫 **Reason:** potential spammer and abuser."
        )

