from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɴʜᴀ̣̂ɴ ᴅᴀɴʜ sᴀ́ᴄʜ ᴛʀᴏ̀ ᴄʜᴜʏᴇ̣̂ɴ ɢɪᴏ̣ɴɢ ɴᴏ́ɪ ʜᴏᴀ̣ᴛ Đᴏ̣̂ɴɢ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ᴋʜᴏ̂ɴɢ ᴄᴏ́ ᴛʀᴏ̀ ᴄʜᴜʏᴇ̣̂ɴ ɢɪᴏ̣ɴɢ ɴᴏ́ɪ ʜᴏᴀ̣ᴛ Đᴏ̣̂ɴɢ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ᴅᴀɴʜ sᴀ́ᴄʜ ᴛʀᴏ̀ ᴄʜᴜʏᴇ̣̂ɴ ɢɪᴏ̣ɴɢ ɴᴏ́ɪ ʜᴏᴀ̣ᴛ Đᴏ̣̂ɴɢ ʜɪᴇ̣̂ɴ ᴛᴀ̣ɪ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» ɴʜᴀ̣̂ɴ ᴅᴀɴʜ sᴀ́ᴄʜ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ʜᴏᴀ̣ᴛ Đᴏ̣̂ɴɢ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ᴋʜᴏ̂ɴɢ ᴄᴏ́ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ʜᴏᴀ̣ᴛ Đᴏ̣̂ɴɢ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ᴅᴀɴʜ sᴀ́ᴄʜ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ Đᴀɴɢ ʜᴏᴀ̣ᴛ Đᴏ̣̂ɴɢ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
