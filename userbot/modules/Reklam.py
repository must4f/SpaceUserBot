# CODER tg/@TheMiri github/@WhoMiri#
# @SPACEUSERBOT / Thanks: TG/Fusuf #
# PLEASE DON'T DELETE THIS LINES (IF YOU KANG) #

from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.reklam ?(.*)")
async def reklam(event):
    if not event.is_reply:
        return await event.edit('```Xaiş edirəm bir mesaja cavap verin...```')
    
    vaxt = event.pattern_match.group(1)
    if (vaxt == ''):
        vaxt = 1.5
    else:
        try:
            vaxt = float(vaxt)
        except:
            vaxt = 1.5
    await event.edit(f'```{vaxt} saniyə gözləyirəm...```')
    mesaj = await event.get_reply_message()
    await event.edit('```Gruplar gətirilir...```')
    gruplar = await event.client.get_dialogs()
    await event.edit(f'```{len(gruplar)} ədət grup tapdım! Gruplar seçilir...```')
    
    i = 0
    for grup in gruplar:
        if grup.is_group:
            await event.edit(f'```{grup.name} grubuna mesajınız göndərilir...```')
            try:
                await grup.send_message(mesaj)
            except:
                await event.edit(f'```❌ {grup.name} grubuna mesajınız göndərilə bilmədi!```')
                await asyncio.sleep(vaxt)
                continue
            i += 1
            await event.edit(f'```✅ {grup.name} grubuna mesajınız göndərildi!```')
            await asyncio.sleep(vaxt)
    await event.edit(f'```✅ {i} ədət gruba mesajınız göndərildi!```')

Komut = CmdHelp('reklam')
Komut.add_command('reklam', '<vaxt>', 'Cavap verdiyiniz mesajı olduğunuz gruplara göndərər.', 'reklam 1')
Komut.add_info('İstəsəniz əmrin yanına vaxt yaza bilərsiniz.')
Komut.add()
