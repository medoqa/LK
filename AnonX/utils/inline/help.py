rom typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="الادمن",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="المصادقه",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="القائمة السوداء",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="اذاعه",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="المحظورين",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="كلمات",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="بينج",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="تشغيل",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="قائمة التشغيل",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="مكالمات الصوتيه",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="بدء",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="المطورين",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ المساعده ❄",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
