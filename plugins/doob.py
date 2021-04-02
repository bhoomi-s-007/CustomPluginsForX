import asyncio
from random import choice

from userge import Message, userge


async def check_and_send(message: Message, *args, **kwargs):
    replied = message.reply_to_message
    if replied:
        await asyncio.gather(message.delete(), replied.reply(*args, **kwargs))
    else:
        await message.edit(*args, **kwargs)


@userge.on_cmd(
    "doob$", about={"header": "A special plugin for our\n@Wasim_ansarii\n😂😂😂"}
)
async def doob_func(message):
    choice(doob)
    stickers = choice(stickers_ids)
    await check_and_send(message, "<b>{}</b>".format(doob), parse_mode="html")
    await message.reply_sticker(sticker="".join(stickers))


doob = """@Wasim_ansarii Doob Maro🥺🥺"""
stickers_ids = (
    "CAACAgEAAx0CVKYprwACRV1gXcNqmPFQwNVcwhxHllfzTEX3JQACOgEAAlSR4EWCGjrKsMOrbB4E",
    "CAACAgEAAx0CVKYprwACRWBgXcOglSa_nlSXP9Tuco_KAAHSmPAAApUAA-Au2EcG3MYpfKPRRh4E",
)
