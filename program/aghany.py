import asyncio

from sys import version_info
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest


@Client.on_message(command(["اغاني"]) & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""🦅 اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="arb")],
                [InlineKeyboardButton("اغاني اجنبي 🇦🇺", callback_data="eng")],
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new"
                    )
                ],
            ]
        ),
    )
