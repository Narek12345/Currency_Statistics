import requests
from bs4 import BeautifulSoup


URL = "https://www.banki.ru/products/currency/cb/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')


# Данные о долларе.
value_usd = soup.find('tr', attrs={"data-currency-code": "USD"})
# Курс доллара.
price_usd = value_usd.select("td:nth-of-type(4)")
# Количества банкнот.
count_usd = value_usd.select("td:nth-of-type(2)")
# Изменение.
change_usd = value_usd.select("td:nth-of-type(5)")


# Данные о евро.
value_euro = soup.find('tr', attrs={"data-currency-code": "EUR"})
# Курс евро.
price_euro = value_euro.select("td:nth-of-type(4)")
# Количества банкнот.
count_euro = value_euro.select("td:nth-of-type(2)")
# Изменение.
change_euro = value_euro.select("td:nth-of-type(5)")


# Данные о драмах.
value_amd = soup.find('tr', attrs={"data-currency-code": "AMD"})
# Курс драма.
price_amd = value_amd.select("td:nth-of-type(4)")
# Количества банкнот.
count_amd = value_amd.select("td:nth-of-type(2)")
# Изменение.
change_amd = value_amd.select("td:nth-of-type(5)")


# Убираем тип данных list.
for price_usd in price_usd:
	price_usd = price_usd

for price_euro in price_euro:
	price_euro = price_euro

for price_amd in price_amd:
	price_amd = price_amd

for count_usd in count_usd:
	count_usd = count_usd

for count_euro in count_euro:
	count_euro = count_euro

for count_amd in count_amd:
	count_amd = count_amd

for count_amd in count_amd:
	count_amd = count_amd

for change_usd in change_usd:
	change_usd = change_usd

for change_euro in change_euro:
	change_euro = change_euro

for change_amd in change_amd:
	change_amd = change_amd


# Готовим данные для импорта в файл bot.py.
USD_DICT = {"Курс": price_usd.text,
			"Количество банкнот": count_usd.text,
			"Изменение": change_usd.text.strip()}

EURO_DICT = {"Курс": price_euro.text,
			"Количество банкнот": count_euro.text,
			"Изменение": change_euro.text.strip()}

AMD_DICT = {"Курс": price_amd.text,
			"Количество банкнот": count_amd.text,
			"Изменение": change_amd.text.strip()}