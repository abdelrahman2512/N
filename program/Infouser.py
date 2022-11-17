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
  usr = await client.get_users(message.from_user.id)
  name = usr.first_name
  namee = usr.last_name
  await message.reply_text("🦅 اسمك الاول » {`{name}`}\n🦅 اسمك الثاني » {`{namee}`}")
