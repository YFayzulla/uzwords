import logging

from aiogram import Bot, Dispatcher, executor, types

from checkWord import checkWords


API_TOKEN ='7481606659:AAF6svDwFa1flZsFYMLuzTLeYJqZ0IbI0Jc'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Uzbek so'zlarini tog'ri yozing!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Botdan foydalanish unchun so'z yuboring!")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text

    # Default response for a specific word
    if word == "емирта":
        await message.answer("Azamat for you ;) yeah in uzbekistan comman word this .!.")
        return

    result = checkWords(word)

    if result['availble']:
        response = f" ✔️ {word}"
    else:
        response = f" ❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f" ✔️ {text.capitalize()}\n"

    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)


    # емирта