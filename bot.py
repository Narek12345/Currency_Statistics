import asyncio
import logging


from parsing import (
	USD_DICT,
	EURO_DICT,
	AMD_DICT)

from aiogram import html
from datetime import datetime
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandObject


# Включаем логирование, чтобы не пропустить важные сообщения.
logging.basicConfig(level=logging.INFO)
# Обьект бота.
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер.
dp = Dispatcher()


# Хэндлер на команду /start.
@dp.message(commands=['start'])
async def start_command(message: types.Message):
	user_name = message.from_user.first_name
	print(user_name)
	await message.answer(f"Привет, {user_name.strip()}.\n\n\
		Узнать курс евро: /euro\n\
		Узнать курс доллара: /usd\n\
		Узнать курс армянского драма: /amd\n\n"\
		"Если нужно помощь ⇒ /help\n\n"\
		"Если вы интересуетесь погодой, мы рекомендуем воспользоваться нашим удобным ботом ⇒ @Weather_Narek_Bot.")


# Хэндлер на команду /help.
@dp.message(commands=['help'])
async def help_command(message: types.Message):
	await message.reply(f"Ваша служба поддержки:\n\n"\
						f"Телеграм адрес ⇒ @Narek_76\n"\
						"Номер телефона ⇒ +79887001838\n\n"\
						"Мы относимся к нашим пользователям с уважением и заботой, так что все данные конфиденциальны. С любовью <b>Currency_Withdrawal</b>.")


# Хэндлер на команду /usd.
@dp.message(commands=['usd'])
async def usd_command(message: types.Message):
	currency = USD_DICT["Курс"]
	count_usd = USD_DICT["Количество банкнот"]
	change = USD_DICT["Изменение"]
	await message.reply(f"Валюта: <b>Доллар</b>\n"\
						f"Курс: <b>{count_usd}$</b> ⇒ <b>{currency}</b> рублей.\n"\
						f"Последние изменения: <b>{change}</b>")


# Хэндлер на команду /euro.
@dp.message(commands=['euro'])
async def euro_command(message: types.Message):
	currency = EURO_DICT["Курс"]
	count_euro = EURO_DICT["Количество банкнот"]
	change = EURO_DICT["Изменение"]
	await message.reply(f"Валюта: <b>Евро</b>\n"\
						f"Курс: <b>{count_euro}€</b> ⇒ <b>{currency}</b> рублей.\n"\
						f"Последние изменения: <b>{change}</b>")


# Хэндлер на команду /amd.
@dp.message(commands=['amd'])
async def amd_command(message: types.Message):
	currency = AMD_DICT["Курс"]
	count_amd = AMD_DICT["Количество банкнот"]
	change = AMD_DICT["Изменение"]
	await message.reply(f"Валюта: <b>Армянский драм</b>\n"\
						f"Курс: <b>{count_amd}֏</b> ⇒ <b>{currency}</b> рублей.\n"\
						f"Последние изменения: <b>{change}</b>")


# Запуск процесса поллинга новых апдейтов.
async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())