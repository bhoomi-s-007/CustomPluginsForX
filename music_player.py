# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import ffmpeg
from pytgcalls import GroupCall
from userge import userge

s = []
group_call = GroupCall(None, play_on_repeat=False)


@userge.on_cmd(
    "playlist",
    about={
        "header": "Play Playlist",
        "description": "Get group playlist ",
        "usage": "{tr}playlist",
    },
)
async def pl(client, message):
    group_call.client = client
    play = await edit_or_reply(message, "`Please Wait!`")
    song = f"**PlayList in {message.chat.title}** \n"
    sno = 0
    if not s:
        if group_call.is_connected:
            await play.edit(f"**Currently Playing :** `{group_call.input_filename}`")
        else:
            await play.edit("`Playlist is Empty Sar And Nothing is Playing Also :(!`")
            return
    if group_call.is_connected:
        song += f"**Currently Playing :** `{group_call.input_filename}` \n\n"
    for i in s:
        sno += 1
        song += f"**{sno})** `{i}` \n"
    await play.edit(song)


@group_call.on_playout_ended
async def playout_ended_handler(group_call, filename):
    global s
    client_ = group_call.client
    if not s:
        await client_.send_message(
            int(f"-100{group_call.full_chat.id}"),
            f"`Finished Playing, No More Playlist Left! :( Leaving VC!`",
        )
        await group_call.stop()
        return
    await client_.send_message(
        int(f"-100{group_call.full_chat.id}"), f"**Now Playing :** `{s[0]}`."
    )
    holi = s[0]
    s.pop(0)
    logging.info("Now Playing " + str(holi))
    group_call.input_filename = holi


@userge.on_cmd(
    ["play", "playmusic"],
    about={
        "header": "Play Music",
        "description": "Play music in voice chat ",
        "usage": "{tr}play reply to an audio file",
    },
)
async def play_m(client, message):
    group_call.client = client
    u_s = await edit_or_reply(message, "`Processing..`")
    if not message.reply_to_message or not message.reply_to_message.audio:
        await u_s.edit("`Reply To Audio To Play It`")
        return
    await u_s.edit_text("`Please Wait, Let Me Download This File!`")
    audio = message.reply_to_message.audio
    audio_original = await message.reply_to_message.download()
    raw_file_name = (
        f"{audio.file_name}.raw" if not audio.title else f"{audio.title}.raw"
    )
    ffmpeg.input(audio_original).output(
        raw_file_name, format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(audio_original)
    if not group_call.is_connected:
        await u_s.edit(f"Playing `{audio.title}...` in {message.chat.title}!")
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            await u_s.edit(f"**Error While Joining VC:** `{e}`")
            return
        group_call.input_filename = raw_file_name
    else:
        s.append(raw_file_name)
        await u_s.edit(f"Added To Position #{len(s)+1}!")


@userge.on_cmd(
    "stopvc",
    about={
        "header": "Stop Voice Chat",
        "description": "Stop the current group voice chat ",
        "usage": "{tr}stopvc",
    },
)
async def kill_vc_(client, message):
    group_call.client = client
    if not group_call.is_connected:
        await edit_or_reply(message, "`Is Group Call Even Connected?`")
        return
    group_call.stop_playout()
    await edit_or_reply(message, "`Stopped Playing Songs!`")


@userge.on_cmd(
    "rvc",
    about={
        "header": "Replay song",
        "description": "Replays song in VC ",
        "usage": "{tr}rvc",
    },
)
async def replay(client, message):
    group_call.client = client
    if not group_call.is_connected:
        await edit_or_reply(message, "`Is Group Call Even Connected?`")
        return
    group_call.restart_playout()
    await edit_or_reply(message, "`Re-Playing!`")


@userge.onon_cmd(
    "rjvc",
    about={
        "header": "Rejoin VC",
        "description": "Rejoins Voice chat ",
        "usage": "{tr}rjvc",
    },
)
async def rejoinvcpls(client, message):
    group_call.client = client
    if not group_call.is_connected:
        await edit_or_reply(message, "`Is Group Call Even Connected?`")
        return
    await group_call.reconnect()
    await edit_or_reply(message, f"`Rejoined! - Vc`")


@userge.on_cmd(
    "leavevc",
    about={
        "header": "Leave Voice Chat",
        "description": "Leaves group VC ",
        "usage": "{tr}leavevc",
    },
)
async def leave_vc_test(client, message):
    group_call.client = client
    if not group_call.is_connected:
        await edit_or_reply(message, "`Is Group Call Even Connected?`")
        return
    await group_call.stop()
    await edit_or_reply(message, f"`Left : {message.chat.title} - Vc`")


@userge.on_cmd(
    "setvolvc",
    about={
        "header": "Set voice chat volume",
        "description": "Sets voice chat volume between 2-100 ",
        "usage": "{tr}setvolvc",
    },
)
async def set_vol(client, message):
    group_call.client = client
    if not group_call.is_connected:
        await edit_or_reply(message, "`Is Group Call Even Connected?`")
        return
    volume = get_text(message)
    if not volume.isdigit():
        await edit_or_reply(message, "Volume Should Be Integer!")
        return
    if int(volume) < 2:
        await edit_or_reply(message, "Volume Should Be Above 2")
        return
    if int(volume) >= 100:
        await edit_or_reply(message, "Volume Should Be Below 100")
        return
    await group_call.set_my_volume(volume)
    await edit_or_reply(message, f"**Volume :** `{volume}`")
