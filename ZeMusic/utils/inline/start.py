
from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𖣂 ضيفني 𖣂", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𖣂 الدعم 𖣂", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" English 🇺🇸 ", callback_data="english"), 
            InlineKeyboardButton(text=" عربي 🇮🇶 ", callback_data="arbic")],
        [
            InlineKeyboardButton(text=" الـمطور ", user_id=config.OWNER_ID),
        ],
    ]
    return buttons
