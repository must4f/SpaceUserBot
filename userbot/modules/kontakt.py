# SpaceUserBot - The Miri

M='kontakt 50'
C=True
G=None
E=len
from telethon.tl.functions.contacts import AddContactRequest as H,GetContactsRequest as B,DeleteContactsRequest as F
from random import sample as I
import asyncio as J
from userbot.events import register as A
from userbot.cmdhelp import CmdHelp as K
D=[]
@A(outgoing=C,pattern='^.addkontakt ?(\\w*)$')
async def L(e):
	M='Space qrupunu kontaktıma əlavə ede bilmerem!!!';C=await e.get_chat();F=await e.client.get_participants(C)
	if e.pattern_match.group(1)=='':
		if E(F)<50:B=round(E(F)/2)
		else:B=50
	else:
		B=int(e.pattern_match.group(1))
		if B>150:await e.client.send_message(-1001158696560,'150dən çox nömrəni kontaktıma salmağa çalışıram!');return
	K=await e.edit(f"`{C.title} qrupundan {B} ədəd istifadəçi kontakta əlavə olunur...`")
	if C.id==-1001158696560 or C.id==-1001259111230:await e.edit('**Əməliyyat Ləğv olundu!**');await e.client.send_message(452321614,M);return
	L=I(F,B)
	for A in L:
		if not A.id in D:
			if A.id==-1001259111230:await e.client.send_message(-1001259111230,M);break
			elif type(A)==G:continue
			await e.client(H(id=A.id,first_name=A.first_name,last_name=A.last_name if A.last_name else'.',phone=''))
		D.append(A.id);await J.sleep(1)
	await K.edit(f"`Təsadüfi seçilən {E(D)} istifadəçi kontakta əlavə olundu!`")
@A(outgoing=C,pattern='^.kontaktsay[ıi]$')
async def N(e):A=await e.client(B(0));A=A.users;await e.edit(f"`{E(A)} nömrə kontaktda var!`")
@A(outgoing=C,pattern='^.kontaktt[eə]mizl[eə]$')
async def L(e):await e.edit(f"`Kontakt Təmizlənir...`");A=await e.client(B(0));await e.client(F(id=A.users));await e.edit(f"`Uğurla Təmizləndi!`")
K('kontakt').add_command('addkontakt','<sayı>','Göstərilən sayda istifadəçini kontakta salar.',M).add_command('kontaktsayi',G,'Kontaktda neçə nəfər olduğunu göstərər.').add_command('kontakttemizle',G,'Kontaktınızı təmizləyər.').add_warning('Tanımadığınız qruplardan icazəsiz şəkildə kontakt vurmağınız qara siyahıya alınmanıza səbəb olacağ!').add_info('Space main modules.').add()
