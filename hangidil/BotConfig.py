from pyrogram import Client, Message
from pyrogram import __version__


class Hangi(Client, Message):
    OWNER_ID: int = 635568322
    CHATS: list = []

    def __init__(self):
        name = self.__class__.__name__.lower()
        print(f"NAME: {name}")
        super().__init__(
            session_name=name,
            config_file=f"hangidil/{name}.ini",
            workers=8,
            plugins=dict(root=f"hangidil/plugins"),
            workdir=f"hangidil/sessions",
        )

        self.admins = {chat: {Hangi.OWNER_ID} for chat in Hangi.CHATS}

    async def start(self):
        await super().start()

        # me = await self.get_me()
        # for chat, admins in self.admins.items():
        #     async for admin in self.iter_chat_members(chat, filter="administrators"):
        #         admins.add(admin.user.id)

    async def stop(self, *args):
        await super().stop()

    # def is_admin(self, message: Message) -> bool:
    #     user_id = message.from_user.id
    #     chat_id = message.chat.id
    #     return user_id in self.admins[chat_id]

