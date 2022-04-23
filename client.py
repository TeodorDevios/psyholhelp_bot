from config import bot, dp
from aiogram import types
from aiogram.dispatcher import Dispatcher


async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет, друг! Несмотря на мое название, я не Аморал! (а хто я?)' +\
                           '\nХочешь поделиться проблемами? Вперед, я помогу! \nНапиши /help и ты поймешь, что дела' +\
                           'ть дальше')


async def help_message(message: types.Message):
    bot.send_message(message.chat.id, 'Итак, мои команды: \n /chat - начать чат\n /stop - остановить чат\n /info -'
                     'узнать информацию о боте и авторе\n /rules - узнать правила использования бота')


def init_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, commands=['help'])
