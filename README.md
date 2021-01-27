
[SUPPORT](https://t.me/SupSpace)

----

<div align="center">
  <img src="https://github.com/whomiri/SpaceInstaller/raw/main/spacelogo.jpg">
  <h1>SPACE UserBot</h1>
</div>
<p align="center">
    Space UserBot, Telegram işlətməyinizi asanlaşdıran bir proyektdir Bütünlüklə açığ yazılım kodlarına sahibdir. Müəllif hüquqları GNU Licence ilə qorunur.
    <br>
        <a href="https://github.com/whomiri/SpaceUserBot/blob/master/README.md#kurulum">Kurulum</a> |
        <a href="https://github.com/Whomiri/SpaceUserBot/wiki/G%C3%BCncelleme">Güncelleme</a> |
        <a href="https://t.me/SpaceUserBot">Telegram Kanalı</a>
    <br>
</p>

----
![Docker Pulls](https://img.shields.io/docker/pulls/fusuf/asenauserbot?style=flat-square) ![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/fusuf/asenauserbot?style=flat-square)
## Qurulum
### Çok Asan Yol
[Youtube Videosu](https://www.youtube.com/watch?v=mUUQ53TYqI0) ![YouTube Video Views](https://img.shields.io/youtube/views/mUUQ53TYqI0?style=flat-square)

**Android:** Termuxu açın ve bu kodu yapışdırın: `bash <(curl -L https://fn.tc/Osii)`

**iOS:** iSH açın ve bu kodu yapışdırın: `apk update && apk add bash && apk add curl && curl -L -o asena_installer.sh https://t.ly/dCsX && chmod +x space_installer.sh && bash space_installer.sh`

**Windows 10:** [Python](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l#activetab=pivot:overviewtab) indirin ardından PowerShell bu kodu yapıştırın: `Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://kutt.it/aYTzCx')`


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/WhoMiri/SpaceUserBot)
### Çətin Yol
```python
git clone https://github.com/WhoMiri/SpaceUserBot.git
cd SpaceUserBot
pip install -r requirements.txt
# Config.env yaradın və düzəldin. #
python3 main.py
```

## Misal Üçün Plugin
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunu yazın bunlar importdur

@register(outgoing=True, pattern="^.yoxlama")
async def deneme(event):
    await event.edit('Yoxlamadan sonraki edit!')

Help = CmdHelp('yoxlama') # Bilgi əlavə etmək isdədiyimizi deyirik
Help.add_command('deneme', # Bura əmr qismini yazırsınız
    None, # Əmr parametri varsa yazın yoxsa None yazın
    'Bu yoxlama Edir!', # Əmr açıqlaması hansiki plugin yüklənəndən sonra Açığlama qismində yazılan
    'deneme' # Misal üçün göstərə biləcəyiniz istifadə tipi.
    )
Help.add_info('@TheMiri tarafından yapılmıştır.') # Bilgi əlavə edirik (burda kim tərəfindən yazılıb və s. bildirə bilərsiniz.
# Ya da Xəbərdarlıq --> Help.add_warning('Xəbərdarlıq!')
Help.add() # Ve Əlavə Edək.
```

## Bilgilendirme
```Bu UserBot yalnızca telegramda daha əyləncəli və yaxşı vaxt keçirin deyə yaradılıb pis yöndə istifadə ettiyiniz təqdirdə Space Səlahiyətliləri olarağ sorumluluğ qəbul etmirik PİS YÖNDƏ İSTİFADƏ ETSƏNİZ ADMİNLƏR TƏRƏFİNDƏN TAPILIB BOTDAN İSTİFADƏ HAQQINIZI ƏLİNİZDƏN ALACAĞIQ!!!```

```
    Userbottan dolayı; Telegram hesabınız bağlana bilər.
    Bu bir açık qaynaqlı proyektdir, yaptığınız her istifadədən özünüz cavabdehsiniz Space Yaradıcıları və Adminləri olarağ heç bir cavabdehlik daşımırıq.
    Space qurarag bu Cavebdihlikleri qebul etmiş sayılırsınız.
```

## Credit
Thanks for;

[Asena UserBot](https://github.com/yusufusta/AsenaUserBot)

