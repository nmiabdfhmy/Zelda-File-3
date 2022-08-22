# (©)Codexbotz
# Recode by @UnrealZlda
# t.me/ZeldaProjects

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"""
<b>Tentang Bot ini :<b>

• <code>Owner     :</code> @UnrealZlda
• <code>Channel   :</code> @ZeldaProjects
• <code>Group     :</code> @HCMutualism
• <code>Source    :</code> <a href='https://t.me/UnrealZlda'>Tanya ke Creator</a>""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass