from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import @Alimboyeevv

router = Router()

# 📋 Menu
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤖 Botni to'liq sozlash")],
        [KeyboardButton(text="💻 Hosting")],
        [KeyboardButton(text="📝 Buyurtma berish")]
    ],
    resize_keyboard=True
)

@router.message(F.text == "/start")
async def start(message: types.Message):
    text = """
🚀 TELEGRAM BOT VA HOSTING XIZMATLARI 🚀

💻 Hosting — 50 000 so'm
🤖 Bot yaratish — 100 000 so'm

👇 Bo'limni tanlang:
"""
    await message.answer(text, reply_markup=menu)

# 📨 Admin ga yuborish (oddiy support)
@router.message(F.text)
async def forward_to_admin(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.bot.send_message(
            ADMIN_ID,
            f"📩 Yangi xabar:\n\n👤 {message.from_user.full_name}\n\n💬 {message.text}"
        )
        await message.answer("✅ Xabaringiz yuborildi, tez orada javob beramiz.")
