import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
from config import USER_OWNER

@app.on_message(
    command(["صورص","سورس","السورس","المملكه الليبيه", "المملكه"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2e7084fa9ccb215044b8a.jpg",
        caption=f"""
𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗦𝗢𝗨𝗥𝗖𝗘 ˛ 𝗔𝗟𝗠𝗮𝗠𝗟𝗔𝗸𝗔 .

اهلا بك في سورس المملڪه الليببه الصوتيه الاكثر سرعه وسيطرة في مجال البوتات الخدميه

لتنصيب بوت ميوزك او حمايه او اي فكرة اخرى راسل مبرمج السورس [اضغط هنا](https://t.me/L_ii_Q)

التواصل مع مبومج السوس للمحظورين [اضغط هنا](https://t.me/H218_BOT)
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/L_ii_Q"), 
                ],[
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/L_B_K1"),
                ],

            ]

        ),

    )
@app.on_message(
   command(["مطور البوت"])
)

@app.on_message(
    command(["المطور"])
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

