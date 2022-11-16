from datetime import datetime
from sys import version_info
from time import time
from driver.veez import user as USER
from config import (
    UPDATES_CHANNEL,
    BOT_USERNAME, 
    SUDO_USERS,
)
from driver.decorators import sudo_users_only
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
import speedtest

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
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(command(["start"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
       await message.reply_text(
                "اهلا عزيزي المطور\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["الاحصائيات"],
                        ["اختبار الحساب المساعد","مغادرة الحساب المساعد من المجموعات"],
                        ["تنصيب php البوت"],
                        ["معلومات السيرفر ","بينج السيرفر","قياس سرعة السيرفر"],
                        ["مدة التشغيل","اعادة تشغيل البوت"],
                        ["طريقة الاذاعة","الغاء التوقف"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
        try:
           await message.reply_photo(
           photo=f"https://t.me/{BOT_USERNAME}",
           caption=f"""✨ **مرحبا {message.from_user.mention()} **\n
💭 **انا بوت استطيع تشغيل الموسيقي والفديو في محادثتك الصوتية
💡 **تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  » 📚 الاوامر !**

🔖 **لتعلم طريقة تشغيلي بمجموعتك اضغط علي » ❓اوامر اساسيه **
معرف الحساب المساعد """,
           reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton("➕ أضفني لمجموعتك ➕",
                           url=f"https://t.me/S88DBOT?startgroup=true",
                       )
                   ],
                   [InlineKeyboardButton("❓ الاوامر الاساسيه", callback_data="cbhowtouse")],
                   [
                       InlineKeyboardButton("📚 الاوامر", callback_data="cbcmds"),
                       InlineKeyboardButton("❤️ المطور", url=f"https://t.me/S150D"),
                   ],
                   [
                       InlineKeyboardButton(
                          "📣 قناة البوت", url=f"https://t.me/FA9SH"
                       ),
                   ],
               ]
             )
           )
        except Exception as error:
           await message.reply_photo(
           photo="https://telegra.ph/file/832677391b763af9c84da.jpg",
           caption=f"""✨ **مرحبا {message.from_user.mention()} **\n
💭 **انا بوت استطيع تشغيل الموسيقي والفديو في محادثتك الصوتية
💡 **تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  » 📚 الاوامر !**

🔖 **لتعلم طريقة تشغيلي بمجموعتك اضغط علي » ❓اوامر اساسيه **
معرف الحساب المساعد @""",
           reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton("➕ أضفني لمجموعتك ➕",
                           url=f"https://t.me/S88DBOT?startgroup=true",
                       )
                   ],
                   [InlineKeyboardButton("❓ الاوامر الاساسيه", callback_data="cbhowtouse")],
                   [
                       InlineKeyboardButton("📚 الاوامر", callback_data="cbcmds"),
                       InlineKeyboardButton("❤️ المطور", url=f"https://t.me/S150D"),
                   ],
                   [
                       InlineKeyboardButton(
                          "📣 قناة البوت", url=f"https://t.me/FA9SH"
                       ),
                   ],
               ]
             )
           )
