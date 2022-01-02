import settings
import logging
# TODO Объединить заголовки и ссылки
from url_parser import HNParser
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton

# Задаём уровень логов
logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API)
dp = Dispatcher(bot)
_parser = HNParser(settings.URL)

get_titles_btn = KeyboardButton('Получить заголовки статей')
get_links_btn = KeyboardButton('Получить ссылки статей')
get_all_btn = KeyboardButton('Получить заголовки со ссылками')

keyboard = ReplyKeyboardMarkup()
keyboard.add(get_titles_btn, get_links_btn, get_all_btn)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer('Давай начнём!', reply_markup=keyboard)


@dp.message_handler()
async def get_commands(message: types.Message):
	if message.text == 'Получить заголовки статей':
		ans = '\n-------------------------------\n'.join(_parser.get_titles())

		await message.answer(ans)

	if message.text == 'Получить ссылки статей':
		ans = '\n-------------------------------\n'.join(_parser.get_links())

		await message.answer(ans)

	if message.text == 'Получить заголовки со ссылками':
		titles = _parser.get_titles()
		links = _parser.get_links()

		ans = ''

		for i in range(len(titles)):
			ans += f'\n{titles[i]}\n({links[i]})\n\n'

		await message.answer(ans)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
