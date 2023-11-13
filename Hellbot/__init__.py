import time
from platform import python_version

from pyrogram import __version__ as pyrogram_version

from .core import LOGS, Config

START_TIME = time.time()


__version__ = {
    "hellbot": "0.3.0",
    "pyrogram": pyrogram_version,
    "python": python_version(),
}


if Config.API_HASH is None:
    LOGS.error("Please set your API_HASH !")
    quit(1)

if Config.API_ID == 0:
    LOGS.error("Please set your API_ID !")
    quit(1)

if Config.BOT_TOKEN is None:
    LOGS.error("Please set your BOT_TOKEN !")
    quit(1)

if Config.DATABASE_URL is None:
    LOGS.error("Please set your DATABASE_URL !")
    quit(1)

if Config.LOGGER_ID == 0:
    LOGS.error("Please set your LOGGER_ID !")
    quit(1)

if Config.OWNER_ID == 0:
    LOGS.error("Please set your OWNER_ID !")
    quit(1)
