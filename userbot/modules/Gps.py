# SpaceUserBot / TheMiri

from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern=r"^.gps (.*)")
async def spacegps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("`Göstərə bilməyim üçün mənə bir yer adı ver.`")

    await event.edit("__Axtarıram__")

    geolocator = Nominatim(user_agent="whomiri")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.reply(
            input_str,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            reply_to=reply_to_id,
        )
        await event.delete()
    else:
        await event.edit("`Bu ərazi tapila bilmedi. :(`")

Help = CmdHelp('gps')
Help.add_command('gps <yer>',  None, 'Seçdiyiniz ərazinin coğrafi yerini göstərər').add()
