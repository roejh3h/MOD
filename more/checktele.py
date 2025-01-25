import random
import threading
import asyncio
from asyncio import sleep
import telethon
from telethon import events, Button
from queue import Queue
import requests
from telethon.sync import functions
from telethon.tl import types
from telethon.tl.types import InputChatUploadedPhoto
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread
import re
a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isfiltering = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1" or choice == "ثلاثي_مختلط":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2" or choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "3" or choice == "vip_رقمين":
        c = random.choices(b)
        d = random.choices(b)
        f = [c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            f = [c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    if choice == "4" or choice == "vip_ثلاث_ارقام":
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            s = random.choices(b)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    if choice == "5" or choice == "vip_اربع_ارقام":
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            s = random.choices(b)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    if choice == "6" or choice == "خماسي_حرف":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "7" or choice == "خماسي_حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "8" or choice == "سداسي_حرف":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "9" or choice == "سداسي_حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "10" or choice == "سباعي_حرف":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "11" or choice == "سباعي_حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "12" or choice == "شبه_سداسي_ارقام_1":
        c = d = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], d[0], s[0], s[0], s[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f = [c[0], d[0], s[0], s[0], s[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "13" or choice == "شبه_سداسي_ارقام_2":
        c = random.choices(b)
        s = random.choices(e)
        d = random.choices(e)
        f = [s[0], d[0], c[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(b)
            s = random.choices(e)
            d = random.choices(e)
            f = [s[0], d[0], c[0], c[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "14" or choice == "شبه_خماسي_1":
        c = random.choices(e)
        s = random.choices(e)
        d = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            s = random.choices(e)
            d = random.choices(e)
            f = [c[0], c[0], c[0], s[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "15" or choice == "شبه_خماسي_2":
        c = random.choices(e)
        s = random.choices(e)
        d = random.choices(e)
        f = [s[0], d[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            s = random.choices(e)
            d = random.choices(e)
            f = [s[0], d[0], c[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "16" or choice == "شبه_خماسي_3":
        c = random.choices(e)
        s = random.choices(e)
        d = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        #random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            s = random.choices(e)
            d = random.choices(e)
            f = [c[0], c[0], c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "17" or choice == "رباعي":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], "_", d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "18" or choice == "خماسي_شرطه":
        c = random.choices(b)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(e)
            f = [c[0], d[0], "_", d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "19" or choice == "سداسي_شرطه":
        c = random.choices(b)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(e)
            f = [c[0], d[0], "_", d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "20" or choice == "بوتات_ثلاثي":
        c = random.choices(e)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "21" or choice == "شبه_ثلاثي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + '_BOT'
        else:
            pass
    if choice == "22" or choice == "شبه_ثلاثي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], d[0], s[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "23" or choice == "رباعي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "24" or choice == "رباعي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "25" or choice == "شبه_رباعي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + '_BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + '_BOT'
        else:
            pass
    if choice == "26" or choice == "شبه_رباعي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], "_"]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "27" or choice == "خماسي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "28" or choice == "خماسي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "29" or choice == "شبه_خماسي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + '_BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + '_BOT'
        else:
            pass
    if choice == "30" or choice == "شبه_خماسي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], "_"]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    if choice == "31" or choice == "رباعي_شرطه":
        c = d = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], "_"]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    return username
    
#############################################################################
#الصيد العادى 
# صيد عدد نوع قناة
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        if choice not in ("ثلاثي_مختلط", "ثلاثي", "vip_رقمين", "vip_ثلاث_ارقام", "vip_اربع_ارقام", "خماسي_حرف", "خماسي_حرفين", "سداسي_حرف", "سداسي_حرفين", "سباعي_حرف", "سباعي_حرفين", "شبه_سداسي_ارقام_1", "شبه_سداسي_ارقام_2", "شبه_خماسي_1", "شبه_خماسي_2", "شبه_خماسي_3", "رباعي", "خماسي_شرطه", "سداسي_شرطه", "بوتات_ثلاثي", "شبه_ثلاثي_1_بوتات", "شبه_ثلاثي_2_بوتات", "رباعي_1_بوتات", "رباعي_2_بوتات", "شبه_رباعي_1_بوتات", "شبه_رباعي_2_بوتات", "خماسي_1_بوتات", "خماسي_2_بوتات", "شبه_خماسي_2_بوتات", "شبه_خماسي_1_بوتات" ,"رباعي_شرطه"):
            if int(choice) < 1 or int(choice) > 31:                                                                                                 
                await event.edit(f"هذا النوع غير موجود")
                isclaim.clear()
                isclaim.append("off")
                trys = 0
                await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        else:
            await event.edit(f"حسناً سأفحص نوع `{choice}` من اليوزرات على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

    for i in range(int(msg[0])):
        if ispay2[0] == 'no':
            break
        username = ""

        username = gen_user(choice)
        t = Thread(target=lambda q, arg1: q.put(
            check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            await asyncio.sleep(1)
            try:
                await TNT(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message("@T_4_S", f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                
                break
            except telethon.errors.FloodWaitError as e:
                hours = e.seconds // 3600
                minutes = (e.seconds % 3600) // 60
                seconds = (e.seconds % 3600) % 60
                message = (
                    f"\"للاسف تبندت\n مدة الباند.\n"
                    f"الساعات: {hours}\n"
                    f"الدقائق: {minutes}\n"
                    f"الثواني: {seconds}\""
                )
                await TNT.send_message(event.chat_id, message)
                await sleep(e.seconds)
                await sleep(20)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except Exception as eee:
                if "(caused by UpdateUsernameRequest)" in str(eee):
                    pass
                elif "the username is already" in str(eee):
                    pass
                elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await TNT.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys = int(trys)
        trys += 3
        
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    await event.client.send_message(event.chat_id, "! انتهى الصيد")
    await event.client.send_message(event.chat_id, "جارى بدء اعدة التشغيل التلقائية بعد الصيد")
    await TNT.disconnect()
    await TNT.send_message(event.chat_id, "`انتهى الصيد و اكتملت اعادة التشغيل التلقائية للسورس بنجاح !`")

#############################################################################

    # الصيد التلقائى بالرد على قناة او انشائها تلقائيا صياد + نوع تلقائى + عدد اليوزرات المطلوب 

@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.صياد (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        TNT_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        choice = str(msg[0])
        tr = int(msg[1]) if len(msg) > 1 and msg[1].isdigit() else 1
        
        if choice not in ("ثلاثي_مختلط", "ثلاثي", "vip_رقمين", "vip_ثلاث_ارقام", "vip_اربع_ارقام", "خماسي_حرف", "خماسي_حرفين", "سداسي_حرف", "سداسي_حرفين", "سباعي_حرف", "سباعي_حرفين", "شبه_سداسي_ارقام_1", "شبه_سداسي_ارقام_2", "شبه_خماسي_1", "شبه_خماسي_2", "شبه_خماسي_3", "رباعي", "خماسي_شرطه", "سداسي_شرطه", "بوتات_ثلاثي", "شبه_ثلاثي_1_بوتات", "شبه_ثلاثي_2_بوتات", "رباعي_1_بوتات", "رباعي_2_بوتات", "شبه_رباعي_1_بوتات", "شبه_رباعي_2_بوتات", "خماسي_1_بوتات", "خماسي_2_بوتات", "شبه_خماسي_2_بوتات", "شبه_خماسي_1_بوتات" ,"رباعي_شرطه"):
            if int(choice) < 1 or int(choice) > 31:                                                                                                 
                await event.edit(f"هذا النوع غير موجود")
                isclaim.clear()
                isclaim.append("off")
                trys = 0
                await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        replly = await event.get_reply_message()

        if tr > 1:

            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶 ▬▭▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟸𝟶 ▬▬▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟹𝟶 ▬▬▬▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟺𝟶 ▬▬▬▬▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟻𝟶 ▬▬▬▬▬▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟼𝟶 ▬▬▬▬▬▬▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟽𝟶 ▬▬▬▬▬▬▬▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟾𝟶 ▬▬▬▬▬▬▬▬▭▭", link_preview=None) 
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟿𝟶 ▬▬▬▬▬▬▬▬▬▭", link_preview=None) 
            await asyncio.sleep(1)
            dl =  await event.edit(f"ᯓ **[TNT Multi HUNTER](t.me/A_0_0_0)**\n**•─────────────────•**\n\n**⇜ انتهي تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶𝟶 ▬▬▬▬▬▬▬▬▬▬💯", link_preview=None)
            await sleep(1)
            await dl.delete()

            for current_cycle in range(tr):
                    try:

                        ch = await TNT(functions.channels.CreateChannelRequest(
                        title="⎉ TNT Hunting Channal ⎉",
                        about=f"This channel to hunt usernames by - @T_4_S , @mmmon {TNT_USER}",
                        ))
            
                        ch = ch.updates[1].channel_id

                        photo = await TNT.upload_file(file="TNT_HUNTER.jpg")
                        await TNT(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))

                        await event.client.send_message(event.chat_id, f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊عدد اليوزرات المطلوبة** {tr} \n**✥┊المحاولة الحالية رقم :- ** {current_cycle + 1} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                    except Exception as e:

                        await TNT.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                        Checking = False
        
        
                    Checking = True
                    while Checking:
                        if ispay2[0] == 'no':
                            break
                        username = ""

                        username = gen_user(choice)
                        t = Thread(target=lambda q, arg1: q.put(
                            check_user(arg1)), args=(que, username))
                        t.start()
                        t.join()
                        isav = que.get()
                        if "Available" in isav:
                            await asyncio.sleep(1)
                            try:
                                await TNT(functions.channels.UpdateUsernameRequest(
                                    channel=ch, username=username))

                                await event.client.send_message(event.chat_id, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                await event.client.send_message("@T_4_S", f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                await event.client.send_message(ch, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')

                                break
                            except telethon.errors.FloodWaitError as e:
                                hours = e.seconds // 3600
                                minutes = (e.seconds % 3600) // 60
                                seconds = (e.seconds % 3600) % 60
                                message = (
                                    f"\"للاسف تبندت\n مدة الباند.\n"
                                    f"الساعات: {hours}\n"
                                    f"الدقائق: {minutes}\n"
                                    f"الثواني: {seconds}\""
                                )
                                await TNT.send_message(event.chat_id, message)
                                await sleep(e.seconds)
                                await sleep(20)
                                pass
                            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                                with open("banned.txt", "a") as f:
                                    f.write(f"\n{username}")
                            except Exception as eee:
                                if "(caused by UpdateUsernameRequest)" in str(eee):
                                    pass
                                elif "the username is already" in str(eee):
                                    pass
                                elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                                    pass
                                else:
                                    await TNT.send_message(
                                        event.chat_id,
                                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                                    )
                                    break
                        else:
                            pass
                        trys = int(trys)
                        trys += 3
            pass
        else:

            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ النـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await TNT(functions.channels.CreateChannelRequest(
                    title="⎉ TNT Hunting Channal ⎉",
                    about=f"This channel to hunt usernames by - @T_4_S , @mmmon {TNT_USER}",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await TNT.upload_file(file="TNT_HUNTER.jpg")
                    await TNT(functions.channels.EditPhotoRequest(
                        channel=ch,
                        photo=photo
                    ))
                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await TNT.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
        
        
            Checking = True
            while Checking:
                if ispay2[0] == 'no':
                    break
                username = ""

                username = gen_user(choice)
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await TNT(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))

                        await event.client.send_message(event.chat_id, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                        await event.client.send_message("@T_4_S", f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                        await event.client.send_message(ch, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')

                        break
                    except telethon.errors.FloodWaitError as e:
                        hours = e.seconds // 3600
                        minutes = (e.seconds % 3600) // 60
                        seconds = (e.seconds % 3600) % 60
                        message = (
                            f"\"للاسف تبندت\n مدة الباند.\n"
                            f"الساعات: {hours}\n"
                            f"الدقائق: {minutes}\n"
                            f"الثواني: {seconds}\""
                        )
                        await TNT.send_message(event.chat_id, message)
                        await sleep(e.seconds)
                        await sleep(20)
                        pass
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        with open("banned.txt", "a") as f:
                            f.write(f"\n{username}")
                    except Exception as eee:
                        if "(caused by UpdateUsernameRequest)" in str(eee):
                            pass
                        elif "the username is already" in str(eee):
                            pass
                        elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                            pass
                        else:
                            await TNT.send_message(
                                event.chat_id,
                                f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                            )
                            break
                else:
                    pass
                trys = int(trys)
                trys += 3
            pass
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    Checking = False
    await event.client.send_message(event.chat_id, "! انتهى الصيد")

#############################################################################
# التحكم بالصيد
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف الصيد"))
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        await event.edit("**- تم إيقـاف عمليـة الصيد .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية صـيد جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
            
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
    if ispay2[0] == "yes":
        if "on" in isclaim:
            await event.edit(f"الصيد وصل لـ({trys}) من المحاولات")
        elif "off" in isclaim:
            await event.edit("لايوجد صيد شغال !")
        else:
            await event.edit("خطأ")
    else:
        pass
#############################################################################
    #تثبيت البوتات
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_بوتات (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])

        if username.startswith('@'): 
            username = username.replace("@", "")  
        else:
            username = username

        if not username.lower().endswith("bot"):
            await event.edit("**● عـذرًا عـزيـزي اليوزر خطـأ ❌**\n**● استخـدم الامـر كالتالـي**\n**● أرسـل (**`..تثبيت_بوتات`** + يوزر البوت نهايته(bot))**")
            isclaim.clear()
            isclaim.append("off")
            trys = ""
            Checking = False
        elif username.lower().endswith("bot"):
            await event.edit(f"تم البدا بنجاح على @{username}")
            Checking = True
            while Checking:
                if ispay2[0] == 'no':
                    break

                t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await TNT.send_message("@BotFather", "/newbot")
                        await asyncio.sleep(1)
                        async for message in TNT.iter_messages("@BotFather", limit=1):
                            if message.message.startswith("Sorry, you can't add more than"):
                                await TNT.send_message(event.chat_id, "لا يمكنك إضافة المزيد من البوتات.")
                                isclaim.clear()
                                isclaim.append("off")
                                trys = ""
                                Checking = False
                                break
                            elif message.message.startswith("Sorry"):
                                match = re.search(r"(\d+) seconds", message.message)
                                if match:
                                    s = int(match.group(1))
                                    hours = s // 3600
                                    minutes = (s % 3600) // 60
                                    seconds = (s % 3600) % 60
                                    message = (
                                        f"\"للاسف تبندت\n مدة الباند.\n"
                                        f"الساعات: {hours}\n"
                                        f"الدقائق: {minutes}\n"
                                        f"الثواني: {seconds}\""
                                    )
                                    await TNT.send_message(event.chat_id, message)
                                    await sleep(s)
                                    await sleep(10)
                            else:
                                await TNT.send_message("@BotFather", "● TNT Bot Hunter ●")
                                await asyncio.sleep(2)
                                await TNT.send_message("@BotFather", f"@{username}")
                                await asyncio.sleep(3)
                                async for message in TNT.iter_messages("@BotFather", limit=1):
                                    if message.message.startswith("Done! Congratulations on your new bot."):
                                        await TNT.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"The user was Hunted by @T_4_S")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", "/setuserpic")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await TNT.send_file("@BotFather", "TNT_HUNTER.jpg")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"TNT Bot Hunted By - @T_4_S , @mmmon")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", "/setdescription")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await TNT.send_message("@BotFather", f"TNT Bot Hunted By - @T_4_S , @mmmon\n owner :-")
                                        
                                        await TNT.send_message(event.chat_id, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ BotFather\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                        await TNT.send_message("@mmmon", f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ BotFather\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                        Checking = False
                                        break
                                    elif message.message.startswith("Sorry, this username is invalid."):
                                        await event.client.send_message(event.chat_id, f"**المعرف @{username} غير صالح !!❌❌**")
                                        isclaim.clear()
                                        isclaim.append("off")
                                        trys = ""
                                        Checking = False
                                        break
                                    else:
                                        pass
                    except Exception as e:
                        print(e)
                else:
                    pass
            trys = int(trys)
            trys += 1
        isclaim.clear()
        isclaim.append("off")
        trys = ""
        Checking = False
        await event.client.send_message(event.chat_id, f"\n- لـ التأكـد قـم بالذهـاب الـى @BotFather\nـ! انتهت عملية تثبيت البوت بنجاح ")
#############################################################################################
# التثبيت التلقائى بالرد على قناة او انشائها تلقائيا 
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_قناة (.*)"))
async def _(event):
    global trys
    trys = 0
    isclaim.clear()
    isclaim.append("on")

    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    username = str(msg[0])

    replly = await event.get_reply_message()
    try:
        
        if replly and replly.text.startswith('@'): 
            
            ch = replly.text
            cmodels = True
            await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ على القناة ( {ch} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
        else:
            user = await event.get_sender()
            uss = user.username   
            TNT_USER = f"@{uss}" if uss else ""
            
            ch = await TNT(functions.channels.CreateChannelRequest(
            title="⎉ TNT Hunting Channal ⎉",
            about=f"This channel to hunt usernames by - @T_4_S , @mmmon | {TNT_USER}",
            ))
                
            ch = ch.updates[1].channel_id
                
            photo = await TNT.upload_file(file="TNT_HUNTER.jpg")
            try:
                await TNT(functions.channels.EditPhotoRequest(
                    channel=ch,
                    photo=photo
                ))
            except Exception:
                pass

            cmodels = True
            await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")

    except Exception as e:
        
        await TNT.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")
        isclaim.clear()
        isclaim.append("off")
        trys = ""
        cmodels = False
        
    if username.startswith('@'): 
        username = username.replace("@", "")  
    else:
        username = username


    isclaim.clear()
    isclaim.append("on")
    cmodels = True
    while cmodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isch = que.get()
        #isch = check_user(username)
        if "Available" in isch:
            try:
                await TNT(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(event.chat_id, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Channel\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message("@T_4_S", f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Channel\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message(ch, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Channel\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                break
            except FloodWaitError as zed:
                wait_time = zed.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except telethon.errors.FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                if "username is already taken" in str(eee):
                    pass
                else:
                    await TNT.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys += 7

        await asyncio.sleep(2)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    
    return await TNT.send_message(event.chat_id, "**- تم الانتهاء من التثبيت .. بنجـاح ✅**")

#############################################################################################
# التثبيت على حساب المستخدم

@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_حساب (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        global trys
        trys = 0
        
        
        ss = str(event.pattern_match.group(1))

        if not ss.startswith('@'): 

            return await event.edit("**✥┊ عـذرًا عـزيـزي المدخـل خطـأ ❌**\n**✥┊ استخـدم الامـر كالتالـي**\n**✥┊ أرسـل (**`.تثبيت_حساب`** + اليـوزر)**")

        
        await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {ss} )**\n**✥┊ نوع التثبيت :- حساب **\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
        
        isclaim.clear()
        isclaim.append("on")
        username = ss.replace("@", "")
        Checking = True
        while Checking:

            isav = check_user(username)

            if "Available" in isav:
                
                try:
                    await TNT(functions.account.UpdateUsernameRequest(username=username))

                    await event.client.send_message(event.chat_id, f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Account\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                    await event.client.send_message("@T_4_S", f'''\n●━━  TNT  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Account\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                    Checking = False
                    break
                except telethon.errors.FloodWaitError as e:
                    hours = e.seconds // 3600
                    minutes = (e.seconds % 3600) // 60
                    seconds = (e.seconds % 3600) % 60
                    message = (
                        f"\"للاسف تبندت\n مدة الباند.\n"
                        f"الساعات: {hours}\n"
                        f"الدقائق: {minutes}\n"
                        f"الثواني: {seconds}\""
                    )
                    await TNT.send_message(event.chat_id, message)
                    await sleep(e.seconds)
                    await sleep(20)
                    pass
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    await event.client.send_message(event.chat_id, f"**المعرف @{username} غير صالح !!❌❌**")
                    isclaim.clear()
                    isclaim.append("off")
                    trys = ""
                    Checking = False
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                    break
                except Exception as eee:
                    
                    if "(caused by UpdateUsernameRequest)" in str(eee):
                        pass
                    elif "the username is already" in str(eee):
                        pass
                    elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                        pass
                    else:
                        await TNT.send_message(
                            event.chat_id,
                            f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                        )
                        Checking = False
                        break
            else:
                pass
            trys = int(trys)
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        Checking = False
        await event.client.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت اليـوزر ع حسـابك .. بنجـاح ✅**")

Threads=[] 
for t in range(200):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()

#############################################################################################
    #التحكم بالتثبيت 
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التثبيت"))
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys1 = 0
        await event.edit("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isclaim:
        await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
############################################################################################
        
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay2[0] == "yes":
        await TNT.send_file(event.chat_id, 'banned.txt')


############################################################################################3
ftrys = 0 
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.تصفية المبند"))
async def filter_banned_users(event):
    global ftrys
    if ispay2[0] == "yes":
        isfiltering.clear()
        isfiltering.append("on")
        replly = await event.get_reply_message()
        try:
            if replly and replly.text.startswith('@'): 
                ch = replly.text
                await event.edit(f"**✥┊سيتم الان تصفية المبند**")
            else:
                user = await event.get_sender()
                uss = user.username   
                TNT_USER = f"@{uss}" if uss else ""
            
                ch = await TNT(functions.channels.CreateChannelRequest(
                title="⎉ TNT Hunting Channal ⎉",
                about=f"This channel to Flood usernames by - @T_4_S , @mmmon | {TNT_USER}",
                ))
            
                ch = ch.updates[1].channel_id
                
                photo = await TNT.upload_file(file="TNT_HUNTER.jpg")
                await TNT(functions.channels.EditPhotoRequest(
                    channel=ch,
                    photo=photo
                ))
                await event.edit(f"**✥┊سيتم الان تصفية المبند**")
        except Exception as e:
            await TNT.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

    try:
        if replly and replly.text.startswith('@'):
            channel_username = replly.text
        else:
            channel_username = ch

        with open("banned.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                username = line.strip()
                try:
                    await TNT(
                        functions.channels.UpdateUsernameRequest(
                            channel=channel_username,
                            username=username
                        )
                    )
                    await event.client.send_message(
                        event.chat_id,
                        f"- Done : @{username} ✅",
                    )
                    await event.client.send_message(
                        "@T_4_S", f"- Done : @{username} ✅",
                    )
                    await event.client.send_message(
                        "@mmmon", f"- Done : @{username} ✅",
                    )
                except telethon.errors.FloodWaitError as e:
                    hours = e.seconds // 3600
                    minutes = (e.seconds % 3600) // 60
                    seconds = (e.seconds % 3600) % 60
                    message = (
                        f"\"للاسف تبندت\n مدة الباند.\n"
                        f"الساعات: {hours}\n"
                        f"الدقائق: {minutes}\n"
                        f"الثواني: {seconds}\""
                    )
                    await TNT.send_message(event.chat_id, message)
                    await sleep(e.seconds)
                    await sleep(20)
                    pass
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    pass
                except Exception as eee:
                    if "The username is already taken" in str(eee) or "USERNAME_PURCHASE_AVAILABLE" in str(eee) or "(caused by UpdateUsernameRequest)" in str(eee):
                        with open("banned.txt", "r+") as f:
                            lines = f.readlines()
                            f.seek(0)
                            for line in lines:
                                if line.strip() != username:
                                    f.write(line)
                            f.truncate()
                    else:
                        await TNT.send_message(
                            event.chat_id,
                            f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                        )
                        break
                ftrys += 1
        ftrys = 0
        isfiltering.clear()
        isfiltering.append("off")
        await TNT.send_file(event.chat_id, 'banned.txt')  # بعد الانتهاء
    except Exception as e:
        await TNT.send_message(event.chat_id, f"خطأ في التصفية , الخطأ**-  : {str(e)}**")


@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التصفية"))
async def check_filter_status(event):
    if ispay2[0] == "yes":
        if "on" in isfiltering:
            await event.edit(f"التصفية وصلت لـ({ftrys}) من المحاولات")
        elif "off" in isfiltering:
            await event.edit("لاتوجد تصفية شغال !")
        else:
            await event.edit("خطأ")
    else:
        pass
################################################################
    #الانواع التقليدية
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع(\d+)?"))
async def show_type(event):
    if ispay2[0] == "yes":
        if event.pattern_match.group(1) is not None:
            type_number = int(event.pattern_match.group(1))
            if type_number == 1:
                await event.edit(Types["Types1"])
            elif type_number == 2:
                await event.edit(Types["Types2"])
            elif type_number == 3:
                await event.edit(Types["Types3"])
        else:
            await event.edit(Types["Types1"])
            
################################################################
    #الانواع التلقائية
@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.النوع(\d+)?"))
async def show_type(event):
    if ispay2[0] == "yes":
        if event.pattern_match.group(1) is not None:
            type_number = int(event.pattern_match.group(1))
            if type_number == 1:
                await event.edit(Auto_Checker["Types1"])
            elif type_number == 2:
                await event.edit(Auto_Checker["Types2"])
            elif type_number == 3:
                await event.edit(Auto_Checker["Types3"])
        else:
            await event.edit(Auto_Checker["Types1"])

@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.ج"))
async def _(event):
    if ispay2[0] == "yes":
        user = await event.get_sender()
        uss = user.username
        uss1 = user.first_name   
        uss2 = user.last_name   
        uss3 = f"{uss1} {uss2}"
        
        uss4 = user.id   
        mention = f"[{uss1}](tg://user?id={uss4})"
        await TNT.send_message(event.chat_id, f"{str(user)}")
        await TNT.send_message(event.chat_id, f"{str(uss)}")
        await TNT.send_message(event.chat_id, f"{str(uss1)}")
        await TNT.send_message(event.chat_id, f"{str(uss2)}")
        await TNT.send_message(event.chat_id, f"{str(uss3)}")
        await TNT.send_message(event.chat_id, f"{str(uss4)}")
        await event.edit(f"""
[⎉ TNT Hunter Source ⎉](t.me/A_0_0_0)
ـ●━━━━━━━━━━━━━━●
✥┊⌔ مـرحبـاً عـزيـزي {mention}
✥┊⌔  إضغـط على الامـر لـنسخه
ـ    ●╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍●
✥┊ .م1   ➪ إعـــدادات الـــســورس 
✥┊ .م2   ➪ أوامــر صيـــد اليوزرات
✥┊ .م3   ➪ أوامــر تثبيت اليوزرات
✥┊ .م4   ➪ أوامــر تـجـمـيـع النقاط
✥┊ .م5   ➪ أوامــر اضافية
ـ●━━━━━━━━━━━━━━●
""", link_preview=None)
        await TNT.send_message(event.chat_id, f'''\n●━━━━━━━━●\n    ┏━━━━━┓\n    - By ↣ @T_4_S , @mmmon\n    ┗━━━━━┛\n    ┏━━━━━┓\n    ↣ user ( @{uss4} )\n    ┗━━━━━┛\n    ┏━━━━━┓\n    -Clicks ↣ ( {uss3} )\n    ┗━━━━━┛\n    ┏━━━━━┓\n    - CH ↣ @A_0_0_0\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')


################################################################
#def generate_navigation_buttons(current_type, max_index):
#    buttons = []
#    if current_type != "Types1":
#        buttons.append(Button.inline("Next", data="next"))
#    if current_type != "Types3":
#        buttons.append(Button.inline("Previous", data="previous"))
#    return buttons

#current_type = "Types1"

#@TNT.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
#async def show_types(event):
#    types_text = Types[current_type]
#    buttons = generate_navigation_buttons(current_type, len(Types))
#    await event.respond(types_text, buttons=buttons)
#
#@TNT.on(events.CallbackQuery(data="next"))
#async def show_next_types(event):
#    global current_type
#    if current_type != "Types1":
#        current_type = f"Types{int(current_type[-1]) + 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)
#
#@TNT.on(events.CallbackQuery(data="previous"))
#async def show_previous_types(event):
#    global current_type
#    if current_type != "Types3":
#        current_type = f"Types{int(current_type[-1]) - 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)
