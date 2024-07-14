# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 

from codewithshubham.must_join import must_join
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    # Check for force subscription
    fsub_status = await must_join(bot, msg)
    if fsub_status == 400:
        return

    me2 = (await bot.get_me()).mention
    picture_url = "https://te.legra.ph/file/1f2ac2fe8cdf202799847.jpg"
    
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=picture_url,
        caption=f"""ʜᴇʏ {msg.from_user.mention},

ɪ ᴀᴍ {me2},
ᴛʀᴜꜱᴛᴇᴅ ꜱᴛʀɪɴɢ ɢᴇɴʀᴀᴛᴏʀ ʙᴏᴛ.
ꜰᴜʟʟʏ ꜱᴀꜰᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ.
ɴᴏ ᴇʀʀᴏʀ.

ᴍᴀᴅᴇ ʙʏ  : [ᴛᴇᴀᴍ ᴄʀᴇᴀᴛᴏʀ](t.me/the_creator_botz) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ 1", url="https://t.me/shubham_X_Official"),
                    InlineKeyboardButton("ᴀᴅᴍɪɴ 2", url="https://t.me/shubham_X_Official")
                ],
                [
                    InlineKeyboardButton(text="ɢᴇɴʀᴀᴛᴇ ꜱᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/the_creator_support_group"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/the_creator_botz")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )

# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 
