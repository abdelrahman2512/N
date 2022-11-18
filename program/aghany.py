import asyncio

from driver.queues import QUEUE
from program import __version__
from driver.veez import user
from config import BOT_USERNAME
from program.utils.inline import menu_markup
from driver.filters import command, other_filters
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery


@Client.on_message(filters.regex(["اغاني"]))
async def aghany_(client: Client, message: Message):
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


@Client.on_callback_query(filters.regex("aghany"))
async def aghany(_, query: CallbackQuery):
    await query.edit_message_text(
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


@Client.on_callback_query(filters.regex("arb"))
async def arb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🦅 اهلا بك بقائمه الفنانين اختر احدي المغنيين\n√
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("مهرجانات 🔊", callback_data="mhrgan"),
                    InlineKeyboardButton("ادهم نابلسي 🔊", callback_data="adhm"),
                ],
                [
                    InlineKeyboardButton("القائمه الرئيسيه ⏺️", callback_data="aghany")],
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new"
                    )
                ],
            ]
        ),
    )
