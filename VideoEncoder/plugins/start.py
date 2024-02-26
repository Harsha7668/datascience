from pyrogram import Client, filters

from .. import (audio, crf, doc_thumb, preset, resolution, sudo_users, tune,
                upload_doc)
from ..utils.utils import check_user, start_but


@Client.on_message(filters.command('start'))
async def start_message(app, message):
    check = await check_user(message)
    if not check:
        return
    text = "Hey! I'm [VideoEncoder](https://telegra.ph/file/11379aba315ba245ebc7b.jpg). I can encode telegram files in x264.\n\nPress /help for my commands :)"
    await message.reply(text=text, reply_markup=start_but, parse_mode="markdownv2")


@Client.on_message(filters.command('help'))
async def help_message(app, message):
    check = await check_user(message)
    if not check:
        return
    msg = """**Commands:**
• AutoDetect Telegram Files.
• /help - Commands List.
• /start - Introduction.
• /vset - View Settings.
• /sthumb - Save Thumb
• /dthumb - Clear Thumb.
• /logs - check logs."""
    await message.reply(text=msg, disable_web_page_preview=True, reply_markup=start_but, parse_mode="markdownv2")


@Client.on_message(filters.command('vset'))
async def vset(app, message):
    check = await check_user(message)
    if not check:
        return
    text = f'''**Encode Settings**
Tune: `{tune}` | `Preset: {preset}`
Audio: `{audio}` | `CRF: {crf}`
Resolution: `{resolution}`

**Upload Settings**
Upload Mode: `{'Document' if (upload_doc) else 'Video' }`
Doc thumb: `{'True' if (doc_thumb) else 'False'}`

**Sudo Users**
`{sudo_users}`
'''
    await message.reply(text=text, reply_markup=start_but, parse_mode="markdownv2")


@Client.on_message(filters.command('logs'))
async def logs(app, message):
    check = await check_user(message)
    if not check:
        return
    file = 'VideoEncoder/utils/logs.txt'
    await message.reply_document(file, caption='#Logs')
