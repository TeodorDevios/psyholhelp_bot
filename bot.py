from aiogram import executor
from config import dp
from client import init_client


async def on_startup(_):
    print('Я работаю, хозяинка')


init_client(dp)
executor.start_polling(dp, skip_updates=True)
