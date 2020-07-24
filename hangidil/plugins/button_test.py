from functools import partial
from pyrogram import Filters, Message, Client, CallbackQuery
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.client.types.bots_and_keyboards.reply_keyboard_markup import (
    ReplyKeyboardMarkup,
)
from pyrogram.client.types.messages_and_media import message

from hangidil.BotConfig import Hangi
from hangidil.utils.helpers import make_buttons

command = partial(Filters.command, prefixes="!")


@Hangi.on_message(command("buton"))
async def buton(client: Client, message: Message):

    buttons = [
        [
            InlineKeyboardButton(text="Mobil Uygulama", callback_data="mobile"),
            InlineKeyboardButton(text="Masaustu Uygulama", callback_data="desktop"),
        ],
        [
            InlineKeyboardButton(text="Oyun", callback_data="dsk_game"),
            InlineKeyboardButton(text="Mobil Oyun", callback_data="mbl_game"),
        ],
        [InlineKeyboardButton(text="Web Gelistirme", callback_data="web")],
    ]

    await client.send_message(
        chat_id=message.chat.id,
        text="Hangi alanla ilgileniyorsun?",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@Hangi.on_message(command("buton2"))
async def buton2(client: Client, message: Message):

    buttons = [
        [
            InlineKeyboardButton(text="Deneme1", callback_data="veri1"),
            InlineKeyboardButton(text="Deneme2", callback_data="veri2"),
        ],
    ]

    await client.send_message(
        chat_id=message.chat.id,
        text="Hangi alanla ilgileniyorsun?",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


def func(_, query: CallbackQuery):
    datas = ["mobile", "desktop", "dsk_game", "mbl_game", "web"]
    return query.data in datas


myFilter = Filters.create(func)


@Hangi.on_callback_query(myFilter)
async def btnCallback(client: Client, callback: CallbackQuery):
    print(callback.from_user.id)
    print(callback.from_user.first_name)
    print(callback.data)
    # @musaitbibot

    # await client.send_message(
    #     chat_id=callback.from_user.id, text=f"Butonun donus verisi: `{callback.data}`"
    # )


def func2(_, query: CallbackQuery):
    datas = ["web", "yapay", "goruntu"]
    return query.data in datas


myFilter2 = Filters.create(func2)


@Hangi.on_callback_query(myFilter2)
async def soru8(client: Client, callback: CallbackQuery):
    print("Diger callback")
    print(callback.from_user.id)
    print(callback.from_user.first_name)
    print(callback.data)
    # @musaitbibot

    # await client.send_message(
    #     chat_id=callback.from_user.id, text=f"Butonun donus verisi: `{callback.data}`"
    # )


@Hangi.on_message(command("test"))
async def test(cl: Client, msg: Message):
    print(f"{msg.from_user.first_name} tikladi :D")
    await cl.send_message(
        chat_id=msg.chat.id,
        text=f"Merhaba **{msg.from_user.first_name}**, [Kaynak Botu](https://t.me/programlama_bot)",
        disable_web_page_preview=True,
        reply_to_message_id=msg.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Bora", callback_data="BORRAM"),
                    InlineKeyboardButton(text="Hakan", callback_data="HAKAN"),
                ],
                [InlineKeyboardButton(text="Burak", callback_data="MUSAITBIYERDE")],
                [InlineKeyboardButton(text="Geri", callback_data="BORA")],
            ]
        ),
    )


def bora(_, query: CallbackQuery):
    return query.data == "BORRAM"


borafilt = Filters.create(bora)


@Hangi.on_callback_query(borafilt)
async def borram(client: Client, callback: CallbackQuery):
    print("BORA Callback")


def hakan(_, query: CallbackQuery):
    datas = ["HAKAN", "MUSAITBIYERDE"]
    return query.data in datas


hakanflt = Filters.create(hakan)


@Hangi.on_callback_query(hakanflt)
async def hakanelb(client: Client, callback: CallbackQuery):
    print("Hakan Callback")

    butons = [
        [InlineKeyboardButton(text="Burak", callback_data="MUSAITBIYERDE")],
        [
            InlineKeyboardButton(text="Hakan", callback_data="HAKAN"),
            InlineKeyboardButton(text="Bora", callback_data="BORRAM"),
        ],
    ]
    await callback.edit_message_text(
        text="Mesaj degisti", reply_markup=InlineKeyboardMarkup(butons),
    )


def filtre_test(_, message: Message):
    datas = ["!buton", "!buton1", "!test"]
    return message.text not in datas


filt_test = Filters.create(filtre_test)


@Hangi.on_message(filt_test)
async def bosfonk(cl: Client, msg: Message):
    print(f"{msg.from_user.first_name} dogru komut girdgiine emin misin?")

    soru_cevap = {
        "soru1": "cevap1",
        "soru2": "cevap2",
        "soru3": "cevap3",
        "soru4": "cevap4",
        "soru5": "cevap5",
    }

    butonlar = make_buttons(answers=soru_cevap, back="HAKAN")

    await cl.send_message(
        chat_id=msg.chat.id,
        text="Sadece buton denemesi",
        reply_markup=InlineKeyboardMarkup(butonlar),
    )
