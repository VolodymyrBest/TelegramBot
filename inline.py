from aiogram import Bot, Dispatcher, types, executor
import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent, InlineQueryResultArticle
from aiogram.dispatcher.filters import Text
import hashlib

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# answ = dict()
#
# urlkb = InlineKeyboardMarkup(row_width=2)
# urlButton = InlineKeyboardButton(text='Ссылка', url='http://youtube.com')
# urlButton2 = InlineKeyboardButton(text='Ссылка2', url='http://google.com')
# x = [InlineKeyboardButton(text='Ссылка3', url='http://google.com'),
#      InlineKeyboardButton(text='Ссылка4', url='http://google.com'),
#      InlineKeyboardButton(text='Ссылка5', url='http://google.com')]
#
# urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='http://google.com'))
#
# inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),
#                                              InlineKeyboardButton(text='DisLike', callback_data='like_-1'))
#
#
# @dp.message_handler(commands=['ссылки'])
# async def urk_command(message: types.Message):
#     await message.answer('Ссылочки: ', reply_markup=urlkb)
#
#
# @dp.message_handler(commands=['test'])
# async def test_command(message: types.Message):
#     await message.answer('За видео', reply_markup=inkb)
#
#
# @dp.callback_query_handler(Text(startswith='like_'))
# async def www_call(callback: types.CallbackQuery):
#     res = int(callback.data.split('_')[1])
#     if f'{callback.from_user.id}' not in answ:
#         answ[f'{callback.from_user.id}'] = res
#         await callback.answer('Вы проголосовали')
#     else:
#         await callback.answer('Вы уже проголосовали', show_alert=True)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'http://ru.wikipedia.org/wiki/' + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Статья Wikipedia',
        url=link,
        input_message_content=types.InputTextMessageContent(message_text=link)
    )]

    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
