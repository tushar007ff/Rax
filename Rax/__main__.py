import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Rax import LOGGER, app, userbot
from Rax.core.call import Rax
from Rax.misc import sudo
from Rax.plugins import ALL_MODULES
from Rax.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Rax.plugins" + all_module)
    LOGGER("Rax.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝...")
    await userbot.start()
    await Rax.start()
    try:
        await Rax.stream_call("https://telegra.ph/file/c6c9e09b6e65b73c35fe4.mp4")
    except NoActiveGroupCall:
        LOGGER("Rax").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n🆂🆃🅾🅿 🆁🅰🆇 🅱🅾🆃........"
        )
        exit()
    except:
        pass
    await Rax.decorators()
    LOGGER("Rax").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎🅼🅰🅳🅴 🅱🆈 🅰🅺🆂🅷🅰🆈🆇🆃☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Rax").info("🆂🆃🅾🅿 🆁🅰🆇 🅼🆄🆂🅸🅲 🎻🅱🅾🆃")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
