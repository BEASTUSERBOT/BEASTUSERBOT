from telethon import events
import beastbot.client
import os


client = beastbot.client.client
alivemsg = "๐๐ข๐ก๐ง ๐ช๐ข๐ฅ๐ฅ๐ฌ ๐ ๐ฌ ๐๐๐๐ฅ๐น\n๐น๐๐ฉ๐๐ ๐๐๐๐ฆ๐ง๐น\n๐น๐ ๐  ๐๐๐๐ฉ๐๐น\n"
  
#beastub = beastbot.resources.beastub
r=(
  
  
  f"๐น{alivemsg}\n\n"
"**โโโโโโโโโโโโโโโโโโโโ**\n\n"
"โผ๐ ๐๐ฆ๐ง๐๐ฅโ๐๐ฉ๐๐ ๐๐๐๐ฆ๐ง\n"
"โโโโโโโโโโโโโโโโโโโโ\n"
"โ โขโณโ  ๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป ๐๐ผ๐ \n"
"โ โขโณโ  ๐ฉ๐ฒ๐ฟ๐๐ถ๐ผ๐ป - ๐ญ.๐ฌ\n"
"โ โขโณโ  `๐๐ต๐ฎ๐ป๐ป๐ฒ๐น:` [๐๐ข๐๐ก](http://t.me/elbeastz_arts)\n"
"โ โขโณโ  `๐๐ฟ๐ฒ๐ฎ๐๐ผ๐ฟ:` [๐๐ฉ๐๐ ๐๐๐๐ฆ๐ง](http://t.me/elbeastz)\n"
"โโโโโโโโโโโโโโโโโโโโ\n"
" [โกShow Power Hereโก](http://t.me/elbeastz)"
  
)

@events.register(events.NewMessage(outgoing=True, pattern=r'\.alive'))

async def alivee(event):
  chat = await event.get_chat()
  await client.delete_messages(chat, event.message)
  photo = 'http://telegra.ph/file/f4c165c958ff3fbbab31b.jpg'
  #photo = await client.download_profile_photo('me')
  #await client.send_file(chat , file=photo , pmcaption=r)   
  await client.send_file(chat , file=photo , caption=r) 
  #os.remove(photo)
