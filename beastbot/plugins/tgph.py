from telethon import TelegramClient, events
import beastbot.client
import os
from html_telegraph_poster import TelegraphPoster
from html_telegraph_poster.upload_images import upload_image


client = beastbot.client.client








tumsg = "ā šš¶š¹š² šØš½š¹š¼š®š±š²š± š§š¼ : "
tumsg2 =( "\nā š§š¶šŗš² š§š®šøš²š» :- š­ š¦š²š° "
  "\nā šš¬ :- [šš©šš šššš¦š§](http://t.me/elbeastz)") 
 

noob = "šššš š¬ššš„!\ššš šš ššš šš¢ š„šš£šš¬ ššš„š”š. \nš”š¢š¢ššš š¢šŖš”šš„š¤¦āāļøš¤¦āāļø"




@events.register(events.NewMessage(outgoing=True, pattern=r'\.upload'))
async def telegraphUploadHandler(event):
  chat = await event.get_chat()
  replied = await event.get_reply_message()
  try:
    image = await replied.download_media()
    x = upload_image(image)
  except:
    return await client.edit_message(event.message,noob ) 
  await client.send_message(chat, tumsg + x + tumsg2)
  os.remove(image)
