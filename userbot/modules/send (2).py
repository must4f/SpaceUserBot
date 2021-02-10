import asyncio
import telethon
from userbot.events import register
from telethon import events
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.send")
async def tm(event):
  if event.is_reply:
    mesaj = await event.get_reply_message()
  else:
    await event.edit("`Bir mesaja cavab verin!`")
    return
  await event.client.forward_messages("me", mesaj)
  await event.edit("`Mesaj` __Kayıtlı Mesajlar__ `bölümünə əlavə olundu`")
  
CmdHelp('send').add_command('send', '<bir mesaja cavab verin>', 'Cavab verdiyiniz mesajı Kayıtlı Mesajlar(Saved Messages) bölümünə göndərər.').add()