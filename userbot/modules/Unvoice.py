# SpaceUserBot - Plugin: @TheMiri #
# Copyright refucion GNU/Licence @SpaceUserBot #
# Thanks @Xacnio #

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from telethon.tl.types import DocumentAttributeAudio
import asyncio
from os import (remove, path)

@register(outgoing=True, pattern="^.[çc]evir voice(?: |$)(.*)")
async def seslimuzik(event):
    caption = "@SpaceUserBot ilə sesli mesaja çevrildi."
    if event.fwd_from:
        return
    sarki = event.pattern_match.group(1)
    rep_msg = None
    if event.is_reply:
        rep_msg = await event.get_reply_message()
    if len(sarki) < 1:
        if event.is_reply:
            sarki = rep_msg.text
        else:
            await event.edit("**Mənə bir mp3 ver!** `İstifadə: .çevir voice _mp3ü yanıtlayın_`") 
            return

    if event.is_reply:
        rep_msg = await event.get_reply_message()
        if rep_msg.audio:
            await event.edit(f"__Səs yüklənir...__")
            indir = await rep_msg.download_media()
            await event.edit(f"__Sesi yüklədim səsli not olarağ göndərirəm...__")
            voice = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' -y -c:a libopus 'unvoice.ogg'")
            await voice.communicate()
            if path.isfile("unvoice.ogg"):
                await event.client.send_file(event.chat_id, file="unvoice.ogg", voice_note=True, caption=caption, reply_to=rep_msg)
                await event.delete()
                remove("unvoice.ogg")
            else:
                await event.edit("`Ses, sesli nota çevrilə bilmədi!`")
            remove(indir)

Komut = CmdHelp('Voice')
Komut.add_command('.çevir voice', '<mp3 reply edin>', 'Replyladığınız mp3ü səsli mesaj olarağ göndərir', '.çevir voice' )
Komut.add_info('Cavap verdiyiniz mp3ü səsli mesaj olarağ atar')
Komut.add()
