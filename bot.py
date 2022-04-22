from aiogram import executor
from config import dp


async def on_startup(_):
    print('Я работаю, хозяинка')


executor.start_polling(dp, skip_updates=True)
