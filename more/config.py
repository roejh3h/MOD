from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = "27455984"
APP_HASH = "62d5f68ce2e9189636967120220f5755"



BOT_USERNAME = "يوزر البوت بدون @"

session = "تيرمكس"

SESSION = "تيرمكس"

token = "التوكن"



TNT = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

