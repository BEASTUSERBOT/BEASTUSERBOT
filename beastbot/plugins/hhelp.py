from telethon import TelegramClient, events, Button
import beastbot.client


client = beastbot.client.client
bot = beastbot.client.bot

@bot.on(events.InlineQuery)
async def iquery(query):
  if query.text == 'help':
    result = query.builder.article('Help', text="šššš£ š šš”šØ š¢š š¹š¹šššš¦š§šš¢š§š¹š¹", buttons=[
      [Button.inline("Alive",data=b'alv'), Button.inline("Hi",data=b'hi')],
      [Button.inline("Reply",data=b'reply'), Button.inline("animation",data=b'anim')],      [Button.inline("arts"), Button.inline("ascii")],      
      [Button.inline("Spam",data=b'spmm'), Button.inline("Upload to tgraph",data=b'uptg')],
      [Button.url("ABOUT DEVELOPER",url = "http://t.me/beastuserbot_dev")]
      
      
      
      
      
          ])
    await query.answer([result])

@bot.on(events.CallbackQuery)
async def call(event):
  
  if event.original_update.user_id == 945846353:
    if event.data == b'alv':
      await event.edit("šš¢ .alive š§š¢ š¦šš šššš©š š šš¦š¦ššš š¢š šššš¦š§ šØš¦šš„šš¢š§")
    if event.data == b'spmm':
      await event.edit("šš¢ .spam [count] [message] š§š¢ š¦š£šš  šš” š šššš§. \n\nšš«šš š£šš : .spam 10 this is beast userbot\n\nšŖšš„š”šš”š! šš¢š”š§ ššš¦š§šØš„š š¢š§ššš„š¦.\nš¬š¢šØš„ šššš¢šØš”š§ ššš” ššš§ ššš šš§šš")
    if event.data == b'uptg':
      await event.edit("šš¢ .upload šš¬ š„šš£šš¬šš”š š šššš \nš§š¢ šØš£šš¢šš šš§ šš” š§ššššš„šš£š")
    if event.data == b'hi':
      await event.edit("šš¢ .hi š§š¢ š¦šš šššš©š š šš¦š¦ššš š¢š šššš¦š§ šØš¦šš„šš¢š§")
    if event.data == b'reply':
      await event.edit("""
      
      š§ššš¦ ššš¦ š ššš¦š§!
      
šš¼ .id  šÆš šæš²š½š¹šš¶š»š“ š® šŗš²ššš®š“š² 
              šš¼ š“š²š šµš¶š ššš²šæš¶š±
              
šš¼ .save  šÆš šæš²š½š¹šš¶š»š“ š® šŗš²ššš®š“š²
         šš¼ š“š²š šµš¶š š½šæš¼š³š¶š¹š² š½š¶š°šššæš²
      """)
    
      
      



  else:
    await event.edit("šŖššš§ š š šš”šØš§š\nšŖšš¢ šš„š š¬š¢šØ ???\n\nšš¢ ššŖšš¬ š”š¢š¢š")
  



@events.register(events.NewMessage(outgoing=True, pattern=r'\.help'))
async def _(event):
  chat = await event.get_chat()
  results = await client.inline_query('@beast_ubot', 'help')
  await results[0].click(entity=chat.id)



