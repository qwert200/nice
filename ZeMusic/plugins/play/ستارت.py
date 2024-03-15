from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from ZeMusic import app as Client
from ZeMusic import app


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f""" انا بوت تشغيل موسيقى صوتية ومرئية .⚡\n
قم بإضافة البوت إلي مجموعتك او قناتك .⚡\n
سيتم تفعيل البوت وانضمام المساعد تلقائياً
في حال مواجهت مشاكل تواصل مع المطور 
استخدم الازرار لمعرفه اوامر الاستخدام .⚡ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت الى مجموعتك ⚡♥",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" الدعم والتواصل ", url=f"https://t.me/ah07v"),
                ],
                [                   InlineKeyboardButton(" طريقه التشغيل ", callback_data="bcmds"),
                    InlineKeyboardButton(" طريقه التفعيل ", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        " الدعم ", url=config.SUPPORT_CHAT
                    ),
                    InlineKeyboardButton(
                        " القناة ", url=config.SUPPORT_CHANNEL),
                ],
                [
                    InlineKeyboardButton(
                        " الـمطور ", user_id=config.OWNER_ID 
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("english"))
async def english(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐴𝑑𝑑 𝑚𝑒 𝑡𝑜 𝑦𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("𝑠𝑢𝑝𝑝𝑜𝑟𝑡 ", url=f"https://t.me/ah07v"),
                ],
                [                
                    InlineKeyboardButton(" 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠", callback_data="cbcmds"),
                    InlineKeyboardButton(" 𝐵𝑎𝑠𝑖𝑐 𝐺𝑢𝑖𝑑𝑒 ", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        " 𝐺𝑟𝑜𝑢𝑝 ", url=config.SUPPORT_CHAT
                    ),
                    InlineKeyboardButton(
                        " 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 ", url=config.SUPPORT_CHANNEL
                    ),
                ],
                [
                    InlineKeyboardButton(
                        " 𝐷𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟 ", user_id=config.OWNER_ID 
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f""" 
 ❓ Basic Guide for using this bot:
1.) First, add me to your group.
2.) Then, promote me as administrator and give all permissions except Anonymous Admin.
3.) After promoting me, type /reload in group to refresh the admin data.
3.) Add Assistant to your group or invite her.
4.) Turn on the video chat first before start to play video/music.
5.) Sometimes, reloading the bot by using /reload command can help you to fix some problem.
📌 If the userbot not joined to video chat, make sure if the video chat already turned on.
💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: https://t.me/ah_2_v
⚡  Developer by ᎪᎻᎷᎬᎠ   
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )


    
    
@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» press the button below to read the explanation and see the list of available commands !
⚡ Powered by ᎪᎻᎷᎬᎠ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Basic Cmd", callback_data="cbsud"),
                ],[
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo")
                ],[
                    InlineKeyboardButton("Go Back ", callback_data="english")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""
🏮 here is the admin commands:\n
» /pause - pause the stream\n
» /resume - resume the stream \n
» /skip - switch to next stream \n
» /stop - stop the streaming \n
» /loop - loop the streaming \n
⚡️  Developer by ᎪᎻᎷᎬᎠ 
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsud"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f""" 
🏮 here is the basic commands:
» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /alive - show the bot alive info (in group)
⚡️  Developer by ᎪᎻᎷᎬᎠ

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f""" 
✏ اوامر المطورين.
» • تعين اسم البوت • 
» • الاحصائيات •
» • المجموعات • 
» • المستخدمين • 
» • قسم الاذاعه •
» • قسم التحكم في الحساب المساعد •
» • تفعيل سجل التشغيل • 
» • تعطيل سجل التشغيل •
» • تغير مكان سجل التشغيل •
» • تفعيل الاشتراك الإجباري • 
» • تعطيل الاشتراك الإجباري • 
» • المكالمات النشطه • 
» • تشغيل مخصص • 
» • اذاعه صوتيه • تغير مكان سجل التشغيل • : لتغير مجموعة السجل
⚡  Developer by ᎪᎻᎷᎬᎠ

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
طريقة تفعيل البوت في مجموعتك ⚡♥️:
1.) اولا قم بإضافة البوت اللي مجموعتك ⚡.
2.) قم بترقية البوت مشرف مع الصلاحيات المطلوبة ⚡.
3.)  يقوم البوت بتحديث قائمة الاداره تلقائياً ⚡.
3.)  قم بإضافة الحساب المساعد اللي المجموعة ⚡.
4.) تاكد من تشغيل المحادثة المرئية ⚡.
📌  اذا لم يستطع الحساب المساعد الانضمام اللي المحادثة المرئيه قم بإعادة تشغيل المحادثه ⚡.
💡 في حال واجهت اي مشكلة اخري يمكنك التواصل مع المطور من هنا : https://t.me/ah07v
⚡  Developer by ᎪᎻᎷᎬᎠ

 """,

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="arbic")]]
        ),
    )


@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
» اتبع الازرار بالاسفل لمعرفة طريقة التشغيل ⚡\n ⚡  Developer by 𝗔𝗛𝗠𝗘𝗗 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="badmin"),
                ],[
                    InlineKeyboardButton("اوامر المطورين", callback_data="bsudo")
                ],[
                    InlineKeyboardButton(" عوده ", callback_data="arbic")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
      اوامر التشغيل ⚡:\n
» شغل او تشغيل - لتشغيل الموسيقى \n  
» فيد او فيديو  - لتشغيل مقطع فيديو \n 
» تشغيل عشوائي  - لتشغيل اغنيه عشوائية \n
» بحث - للبحث عن نتائج في اليوتيوب \n
» حمل + اسم الفيديو - لتحميل مقطع فيديو \n
» نزل + اسم الاغنيه - لتحميل ملف صوتي \n
» اغاني - جلب قائمة الاغاني والفنانين \n
» تفعيل الاذان - تفعيل تنبيهات الصلاة في المحادثه \n
» بنج - عرض سرعة الاستجابة \n
» سورس - لعرض معلومات البوت \n
⚡️  Developer by ᎪᎻᎷᎬᎠ  
        """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="bcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
      اوامر التحكم للخاصة بالادمنية: \n
» ايقاف مؤقت - ايقاف التشغيل موقتأ \n
» استكمال - لاستكمال التشغيل \n
» تخطي - لتخطي تشغيل الحالي \n
» ايقاف او اسكت - لايقاف تشغيل الحالي \n
» تكرار او كررها - لتكرار التشغيل الحالي \n
» تمرير او مرر - لتتغير وقت التشغيل الحالي\n
⚡️  Developer by ᎪᎻᎷᎬᎠ  
        """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="bcmds")]]
        ),
    )
    

@Client.on_callback_query(filters.regex("bsudo"))
async def acbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
       ✏ اوامر المطورين.\n
» • تعين اسم البوت • \n
» • الاحصائيات •\n
» • المجموعات • \n
» • المستخدمين • \n
» • قسم الاذاعه •\n
» • قسم التحكم في الحساب المساعد •\n
» • تفعيل سجل التشغيل • \n
» • تعطيل سجل التشغيل •\n
» • تغير مكان سجل التشغيل •\n
» • تفعيل الاشتراك الإجباري • \n
» • تعطيل الاشتراك الإجباري • \n
» • المكالمات النشطه • \n
» • تشغيل مخصص • \n
» • اذاعه صوتيه • 

⚡  Developer by ᎪᎻᎷᎬᎠ 
        """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="bcmds")]]
        ),
    )
