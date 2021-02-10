# Code by: @s1rvann 
# İcazəsiz Oğurlama Oğul!
from datetime import datetime
from speedtest import Speedtest
from telethon import functions
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import os
from requests import get

@register(outgoing=True, pattern="^.suret$")
@register(outgoing=True, pattern="^.sürət$")
async def cspeedtstimg(spd):
    test = Speedtest()
    MESSAGE = ""
    try:
        await spd.edit("`Sürət Testinin Server Məlumatı Gətirilir Gözləyiniz...`")
        test.get_best_server()
    except:
        await spd.edit("`Sürət Testinin Server Məlumatı Təkrar Gətirilir !...`")
        try:
            test.get_best_server()
        except:
            return await spd.edit("`Sürət Testinin Server Məlumatı Gətirilə bilmədi!?/`")

    MESSAGE = "**Server:** `"+test.results.server['sponsor']+"("+test.results.server['name']+")`"
    await spd.edit(MESSAGE + "\n**Yükləmə Sürəti**: `Test Edilir!...`")
    test.download()
    MESSAGE += "\n**Yükləmə Sürəti**: `"+"%0.2f Mbit/s`" % (float(test.results.dict()['download'])  / 1000.0 / 1000.0)
    await spd.edit(MESSAGE + "\n**Yükləmə Sürəti**: `Test edilir...`")
    test.upload()
    MESSAGE += "\n**Yükləmə Sürəti**: `"+"%0.2f Mbit/s`" % (float(test.results.dict()['upload']) / 1000.0 / 1000.0)
    MESSAGE += "\n**Ping**: `"+"%0.3f ms`" % float(test.results.dict()['ping'])
    MESSAGE += "\n**ISP**: "+ "`%s`" % str(test.results.dict()['client']['isp'])
    await spd.edit(MESSAGE + "\n`Test məlumatı hazırlanır...`")
    test.results.share()
    if os.path.exists("@UseratorUserBot-Cspeed.jpg"):
        os.remove("@UseratorUserBot-Cspeed.jpg")

    try:
        r = get(test.results.share())
        with open("@UseratorUserBot-Cspeed.jpg", 'wb') as f:
            f.write(r.content)    
        await spd.client.send_file(spd.chat_id, file="@UseratorUserBot-Cspeed.jpg", force_document=False, caption=MESSAGE)
        os.remove("@UseratorUserBot-Cspeed.jpg")
        await spd.delete()
    except:
        await spd.edit(MESSAGE)


CmdHelp('speedtest').add_command(
    'sürət', None, 'Sürət testi edər və nəticələri şəkil kimi göndərər.'
).add()