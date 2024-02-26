from pyrogram import Client, filters

from .. import (audio, crf, doc_thumb, preset, resolution, sudo_users, tune,
                upload_doc)
from ..utils.utils import check_user, start_but


@Client.on_message(filters.command('start'))
async def start_message(app, message):
    check = await check_user(message)
    if not check:
        return
    text = "Hey! I'm <a href='https://telegra.ph/file/11379aba315ba245ebc7b.jpg'>VideoEncoder</a>. I can encode telegram files in x264.\n\nPress /help for my commands :)"
    await message.reply(text=text, reply_markup=start_but, parse_mode="html")


@Client.on_message(filters.command('help'))
async def help_message(app, message):
    check = await check_user(message)
    if not check:
        return
    msg = """<b>Commands:</b>
• AutoDetect Telegram Files.
• /help - Commands List.
• /start - Introduction.
• /vset - View Settings.
• /sthumb - Save Thumb
• /dthumb - Clear Thumb.
• /logs - check logs."""
    await message.reply(text=msg, disable_web_page_preview=True, reply_markup=start_but, parse_mode="html")


@Client.on_message(filters.command('vset'))
async def vset(app, message):
    check = await check_user(message)
    if not check:
        return
    text = f'''<b>Encode Settings</b>
Tune: <code>{tune}</code> | <code>Preset: {preset}</code>
Audio: <code>{audio}</code> | <code>CRF: {crf}</code>
Resolution: <code>{resolution}</code>

<b>Upload Settings</b>
Upload Mode: <code>{'Document' if (upload_doc) else 'Video' }</code>
Doc thumb: <code>{'True' if (doc_thumb) else 'False'}</code>

<b>Sudo Users</b>
<code>{sudo_users}</code>
'''
    await message.reply(text=text, reply_markup=start_but, parse_mode="html")


@Client.on_message(filters.command('logs'))
async def logs(app, message):
    check = await check_user(message)
    if not check:
        return
    file = 'VideoEncoder/utils/logs.txt'
    await message.reply_document(file, caption='#Logs')
