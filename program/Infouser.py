import asyncio

from sys import version_info
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest


@Client.on_message(
    command(["اسمي"])
    & ~filters.edited
)
async def muamen(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""🦅 اسمك الاول » ❲`{message.from_user.first_name}`❳\n🦅 اسمك الثاني » ❲`{message.from_user.last_name}`❳""")


@Client.on_message(
    command(["رتبتي"])
    & ~filters.edited
)
async def m(client: Client, message: Message):
    if message.from_user.id == "1970797144":
        await message.reply_text("مبرمج السورس")
