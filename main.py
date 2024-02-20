from aiogram import Bot, Dispatcher, types, utils
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN_API = "6983493370:AAF2mYxJalVUolOrQi4C6wF3WrNpbajS9JM"
is_voted = False
ikb = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton('❤️', callback_data='like'), InlineKeyboardButton('💔', callback_data='dislike')],
  [InlineKeyboardButton('Close keyboard', callback_data='close')]
])
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
  await bot.send_photo(chat_id=message.from_user.id,
                       photo='https://images.unsplash.com/photo-1601979031925-424e53b6caaa?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cHVwcHl8ZW58MHx8MHx8fDA%3D',
                       caption='Do you like this photo?',
                       reply_markup=ikb)
  
  
@dp.callback_query_handler(text='close')
async def ikb_close_cb_handler(callback: types.CallbackQuery):
  await callback.message.delete()

@dp.callback_query_handler()
async def ikb_close_cb_handler(callback: types.CallbackQuery):
  global is_voted
  if not is_voted:
    if callback.data == 'like':
      await callback.answer(show_alert=False,
                            text=str(callback.data))
      is_voted = True
    else:
      await callback.answer(show_alert=False,
                            text=str(callback.data))
      is_voted = True
  else:
    await callback.answer(show_alert=True,
                          text='You have aleady voted!')

if __name__ == "__main__":
  executor.start_polling(dispatcher=dp,
                         skip_updates=True)
  
  