from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني في قروبك ولا قناتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعده",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="الاعدادات", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني في قروبك ولا قناتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة السورس",
                url=f"https://t.me/",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعده", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ قروب الدعم ❣", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 المطور 🥀", user_id=OWNER
            )
        ]

    return buttons
