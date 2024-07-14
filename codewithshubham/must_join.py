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
from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

# This function checks if a user is a member of a required channel before allowing them to interact with the bot
@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    # If MUST_JOIN is not set, the function returns and does nothing
    if not MUST_JOIN:
        return

    try:
        # Check if the user is a member of the MUST_JOIN channel
        await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
    except UserNotParticipant:
        # If the user is not a participant, generate the invite link
        if MUST_JOIN.isalpha():
            # If MUST_JOIN is an alphanumeric string, concatenate it to the base link
            link = f"https://t.me/{MUST_JOIN}"
        else:
            # Otherwise, get the chat info and use its invite link
            chat_info = await bot.get_chat(MUST_JOIN)
            link = chat_info.invite_link

        try:
            # Send a message prompting the user to join the channel with an invite link
            await msg.reply_photo(
                photo="https://telegra.ph/file/c05c0889dcd0c1054de3f.jpg", 
                caption=f"» ғɪʀsᴛ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ [𝖩𝖮𝖨𝖭]({link}) ᴀғᴛᴇʀ Jᴏɪɴ sᴛᴀʀᴛᴇᴅ ᴍᴇ ᴀɢᴀɪɴ !",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ", url=link),
                        ]
                    ]
                )
            )
            # Stop further propagation of the message if the user is not a participant
            await msg.stop_propagation()
        except ChatWriteForbidden:
            # If the bot cannot write in the chat, handle the error silently
            pass
    except ChatAdminRequired:
        # If the bot is not an admin in the MUST_JOIN chat, print a warning message
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")

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
