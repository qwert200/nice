import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings.filters import command
from config import BANNED_USERS
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest
import config
from ZeMusic import app
from ZeMusic.utils.inline import help_pannel, private_panel, start_panel
from strings import get_string




REPLY_MESSAGE = "**- اهلا بك عزيزي اليك قائمه الاوامر**"




REPLY_MESSAGE_BUTTONS = [

         [

             ("‹ اوامر التشغيل ›"),                   

             ("‹ اوامر التفعيل ›")




          ],

          [

             ("‹ اوامر التسليه ›"),

             ("‹ السورس ›")

          ],

          [

             ("اخفاء الازرار")

          ]

]



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply("**- بخدمتك حجي خفيت الازرار\n- اذا تريد تطلعها مرة ثانية اكتب الاوامر**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("طريقة ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/Source_Ze"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
