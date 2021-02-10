import re
import os
from telethon import events
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("yetkaspace")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.pm ?(.*)")
async def pm(event):
 
    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:  
        chat_id = int(chat_id)
    except BaseException:
        
        pass
  
    msg = ""
    mssg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit(LANG['PM_ACSESS'])
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit(LANG['PM_ACSESS'])
    except BaseException:
        await event.edit(LANG['PM_QEUIC'])
        
CmdHelp('pm').add_command(
    'pm', '<istifadəçi adı> <mesaj>', 'Verdiyiniz mesajı seçdiyiniz şəxsə göndərər', '.pm @TheMiri Sammekim'
).add()
