from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"It's not that complicated😅 \n\nSend Me Youtube Link To Be Uploaded To Telegram. \n\nAnd just select resolution and click on video/document which you want to be uploaded."
    await message.reply_text(helptxt)
