from pyrogram import filters
from typing import List, Union
from config import COMMAND_PREFIXES


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded & ~filters.regex
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded & ~filters.regex
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
