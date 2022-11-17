import asyncio

from sys import version_info
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest


@Client.on_message(command(["اسمي"]))
async def muamen(client: Client, message: Message):
    await message.reply_text("🦅 اسمك الاول » {{message.from_user.first_name}}\n🦅 اسمك الثاني » {️{message.from_user.last_name}}")
