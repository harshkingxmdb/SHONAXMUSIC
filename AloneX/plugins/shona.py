# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AloneXMusic


from pyrogram import filters, types

from AloneX import app


@app.on_message(filters.video_chat_members_invited & filters.group)
async def _vc_invited(_, message: types.Message):
    text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "

    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
        except Exception:
            pass

    try:
        await message.reply(f"{text} 😉")
    except Exception:
        pass
