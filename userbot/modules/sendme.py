import asyncio
import telethon
from userbot.events import register
from telethon import events
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("yetkaspace")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.sendme")
@register(outgoing=True, pattern="^.kaydet")
@register(outgoing=True, pattern="^.qeydet")
@register(outgoing=True, pattern="^.kayıtlı")
async def ok(event):
  if event.is_reply:
    mesaj = await event.get_reply_message()
  else:
    await event.edit(LANG['YOLLAMA_MENE'])
    return
  await event.client.forward_messages("me", mesaj)
  await event.edit(LANG['YOLLA_MENE'])
  
CmdHelp('send').add_command('send', '<bir mesaja cavab verin>', 'Cavab verdiyiniz hər nəyisə kayıtlı mesajlarınıza atar.').add()
