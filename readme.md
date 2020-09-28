h1 Описание методов
---
h2 файл script.py
***
Создает локальный сервер по адресу 127.0.0.1:8000.
---
h2 файл index.html
***
Главная страница на которой отображаются три модуля.
---
h2 файл form.py
***
Выводит найденые значения по введеному geonameid.
---
h2 файл form_second.py
***
Выводит страницу и отображает переданное число городов.
Так же реализована пагинация.
---
h2 файл form_third.py
***
Выводит 2 города найденные по русскому наименованию.
Выводится какой город севернее, в одном ли часовом поясе.
Так же реализовано дополнительное задание:
Выполнено вычесление, на сколько отличается временной интервал у городов.
---
h2 файл read.py
***
Основной файл где хранятся функции и происходят вычисления.
***
h4 download_list()
Функция подгружает данные из файла записывая данные по городу в словарь,
а затем записывающая данные в список.
***
h4 search_list(value)
Функция ищет geonameid в списке из словарей и возвращает найденный словарь.
***
h4 search_pages(page, amount_citys)
Функция выводит указанную страницу с указаным количеством городов на ней.
***
h4 city_comparison(first_city, second_city)
Функция находит 2 города введеных на руском языке и возвращает их словари.
***
h4 time_zone_search(first_time_zone, second_time_zone)
Функция определяет на сколько отличается время у первой и второй зоны
от гринвича, а затем возвращает разницу между ними
