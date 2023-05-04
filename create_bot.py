from aiogram import Bot, Dispatcher
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot, storage=storage)

