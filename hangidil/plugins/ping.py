import time
from functools import partial
from pyrogram import Filters, Message, Client
from hangidil.BotConfig import Hangi

command = partial(Filters.command, prefixes="!")


@Hangi.on_message(command("ping"))
async def ping(client: Client, message: Message):
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"**Pong!** `{delta_ping * 1000:.3f} ms`")

