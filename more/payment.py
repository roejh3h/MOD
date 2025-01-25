from config import *
from telethon import events
from help import *


@TNT.on(events.NewMessage(outgoing=True))
async def _(event):
    #message_sent = False
    #if not message_sent:
    #    await TNT.send_message("@T_4_S", f'''تم بدأ السورس بنجاح
    #                                  ايها المطور @T_4_S''')
    #    message_sent = True
        
    id = str(event.sender_id)
    idas = await TNT.get_messages("sedupay", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("yes")
    elif id not in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("yes")
    else:
        pass

    id = str(event.sender_id)
    idas = await TNT.get_messages("sedupay2", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay2[0] == 'yes':
        ispay2.clear()
        ispay2.append("yes")
    elif id not in msg and ispay2[0] == 'yes':
        ispay2.clear()
        ispay2.append("yes")
    else:
        pass
