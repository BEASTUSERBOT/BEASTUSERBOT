
from telethon import TelegramClient, events
import beastbot.client
client = beastbot.client.client

@events.register(events.NewMessage(outgoing=True, pattern='hi$'))
async def _(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, "šš²š¹š¹š¼! šš¼š š®šæš² šš¼š.")
  
@events.register(events.NewMessage(outgoing=True, pattern='hey$'))
async def _2(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, "šš²š¹š¹š¼?\nššššš¢ š©š„š¢?\nšš„š š¬š¢šØ š¢š”ššš”š?")
  

