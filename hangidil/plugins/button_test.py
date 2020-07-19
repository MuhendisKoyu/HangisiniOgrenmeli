from functools import partial
from pyrogram import Filters, Message, Client, CallbackQuery
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup
from hangidil.BotConfig import Hangi

command = partial(Filters.command, prefixes="!")


@Hangi.on_message(command("buton"))
async def buton(client: Client, message: Message):

    buttons = [
        [InlineKeyboardButton(text="Mobil Uygulama", callback_data="mobile")],
        [InlineKeyboardButton(text="Masaustu Uygulama", callback_data="desktop")],
        [InlineKeyboardButton(text="Oyun", callback_data="dsk_game")],
        [InlineKeyboardButton(text="Mobil Oyun", callback_data="mbl_game")],
        [InlineKeyboardButton(text="Web Gelistirme", callback_data="web")],
    ]

    await client.send_message(
        chat_id=message.chat.id,
        text="Hangi alanla ilgileniyorsun?",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


def func(_, query):
    datas = ["mobile", "desktop", "dsk_game", "mbl_game", "web"]
    return query.data in datas


myFilter = Filters.create(func)


@Hangi.on_callback_query(myFilter)
async def btnCallback(client: Client, callback: CallbackQuery):
    print(callback.data)

    await client.send_message(
        chat_id=callback.from_user.id, text=f"Butonun donus verisi: `{callback.data}`"
    )
