import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6001520005:AAFYFbOvhZAfeuwELoYE2WGiNQGWqA3Eh1E"
MSG_GOOD = "\U00002705 Yes, this SN in the base. Checked!"
MSG_BAD = "\U0000274C No, this SN is not in the base. Fixed."

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

f = open("baseserials.td", "r")
serialsN = f.read()
f.close()


@dp.message_handler(commands=['start'])
async def start(message):

    # user_full_name = message.from_user.full_name
    await message.reply("Hello, I am your bot. Opt: /start /allsn /serials /clean")


@dp.message_handler(commands=['clean'])
async def start(message):
    f = open("all_sn.td", "w")
    f.write("")
    f.close()
    await message.reply("All SN in file was cleared!")


@dp.message_handler(commands=['allsn'])
async def start(message):
    f = open("all_sn.td", "r")
    text = f.read()
    f.close()
    await message.reply(text)


@dp.message_handler(commands=['serials'])
async def start(message):
    await message.reply(serialsN)


@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    user_id = message.from_user.id
    if message.text in serialsN:
        await bot.send_message(user_id, MSG_GOOD)
        f = open("all_sn.td", "a")
        f.write("*** " + message.text + " ***\n")
        f.close()
    else:
        await bot.send_message(user_id, MSG_BAD)
        f = open("all_sn.td", "a")
        f.write(message.text + "\n")
        f.close()


if __name__ == '__main__':
    executor.start_polling(dp)
