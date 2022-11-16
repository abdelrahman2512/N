import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://vampir:Al2552001@cluster0.yeaoc.mongodb.net/vampir?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "S150D")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FA9SH")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ttqqk/N")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
