from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» ᴛᴜ̛̣ Đᴏ̣̂ɴɢ ᴋᴇ̂́ᴛ ᴛʜᴜ́ᴄ sᴛʀᴇᴀᴍ Đᴀ̃ ʙᴀ̣̂ᴛ.\n\nᴛʀᴏ̛̣ ʟʏ́ sᴇ̃ ᴛᴜ̛̣ Đᴏ̣̂ɴɢ ʀᴏ̛̀ɪ ᴋʜᴏ̉ɪ ᴠɪᴅᴇᴏᴄʜᴀᴛ sᴀᴜ ᴠᴀ̀ɪ ᴘʜᴜ́ᴛ ᴋʜɪ ᴋʜᴏ̂ɴɢ ᴄᴏ́ ᴀɪ ɴɢʜᴇ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» ᴛᴜ̛̣ Đᴏ̣̂ɴɢ ᴋᴇ̂́ᴛ ᴛʜᴜ́ᴄ sᴛʀᴇᴀᴍ Đᴀ̃ ᴛᴀ̆́ᴛ.")
    else:
        await message.reply_text(usage)
