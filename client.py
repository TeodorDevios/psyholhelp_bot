from config import bot, dp
from aiogram import types
from aiogram.dispatcher import Dispatcher


async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет, друг! Несмотря на мое название, я не Аморвл! (а хто я?)' +\
                           '\nХочешь поделиться проблемами? Вперед, я помогу! Напиши /help и ты поймешь, что делать ' +\
                           'дальше')


def init_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
