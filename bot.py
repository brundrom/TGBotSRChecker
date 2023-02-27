import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "6001520005:AAFYFbOvhZAfeuwELoYE2WGiNQGWqA3Eh1E"
MSG_GOOD = "Yes, this SN on the Igor. Checked!"
MSG_BAD = "No, this SN is not Igor. Fixed."

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
serialNum = "2"


@dp.message_handler(commands=['start'])
async def start(message):

    # user_full_name = message.from_user.full_name
    await message.reply("Hello, I am your bot helper")


@dp.message_handler(commands=['clean'])
async def start(message):
    f = open("all_sn.td", "w")
    f.write("")
    f.close()
    await message.reply("All SN in file was cleared!")


@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    user_id = message.from_user.id
    if message.text == '2345':
        await bot.send_message(user_id, MSG_GOOD)
    else:
        await bot.send_message(user_id, MSG_BAD)
        f = open("all_sn.td", "a")
        f.write(message.text)
        f.close()

if __name__ == '__main__':
    executor.start_polling(dp)
