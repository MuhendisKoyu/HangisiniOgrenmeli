from pyrogram import InlineKeyboardButton


def slicer(button_list: list, size: int = 2) -> list:
    return [button_list[i : i + size] for i in range(0, len(button_list), size)]


def make_buttons(answers: dict, size: int, back: str) -> list:

    buttons: list = [
        InlineKeyboardButton(text=k, callback_data=v) for k, v in answers.items()
    ]
    buttons = slicer(buttons, size)

    if back:
        back_button: InlineKeyboardButton = InlineKeyboardButton(
            text="Geri", callback_data=back
        )
        buttons.append([back_button])

    return buttons
