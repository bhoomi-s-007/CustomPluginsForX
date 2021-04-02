# Copyright (C) 2020-2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime

from userge import Message, get_version, userge


@userge.on_cmd(
    "hie",
    about={
        "header": "check pingtime, uptime and version of your userbot",
        "flags": {"-a": "average ping"},
    },
    group=-1,
)
async def heyme(message: Message):
    start = datetime.now()
    await message.edit("`Hillo!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    up_time = userge.uptime
    ub_version = get_version()
    await message.edit(
        f"**Hillo!**\nPing :` {m_s} m`\nUptime :` {up_time}`\nVersion :` {ub_version}`"
    )
