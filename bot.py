import config
import time
import logging
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)

StartTime = time.time()
app = Client(
    "DAXX",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="codewithshubham"),
)


if __name__ == "__main__":
    print("ꜱᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ꜱᴛʀɪɴɢ ʙᴏᴛ ...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ. ᴍᴀᴅᴇ ʙʏ @The_creator_Botz 🤗")
    idle()
    app.stop()
    print("ʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ!")
