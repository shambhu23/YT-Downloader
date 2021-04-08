from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Developer", url="https://t.me/Gauranga_108")]
    ])
    welcomed = f"Hare Kṛṣṇa <b>{message.from_user.first_name}</b> 🙏🏻 \n\nYo, I am a Powefull Youtube Downloader Bot 🤓! \n\nSend Me Youtube Link, So I Can Upload It To Telegram As File/Video! \n\nAny Help > /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
