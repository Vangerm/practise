from math import ceil

def download_list():
	"""
		Функция подгружающая данные из файла
		записывая данные по городу в словарь,
		а затем записывающая данные в список
	"""
	global citys
	citys = []
	dict = {}
	with open('RU.txt', 'r', encoding='utf-8') as file:
		for i in file.read().splitlines():
			a = i.split('\t')
			dict['geonameid'] = a[0]
			dict['name'] = a[1]
			dict['asciiname'] = a[2]
			dict['alternatenames'] = a[3].split(',')
			dict['latitude'] = a[4]
			dict['longitude'] = a[5]
			dict['feature_class'] = a[6]
			dict['feature_code'] = a[7]
			dict['country_code'] = a[8]
			dict['cc2'] = a[9]
			dict['population'] = a[14]
			dict['elevation'] = a[15]
			dict['dem'] = a[16]
			dict['timezone'] = a[17]
			dict['modification_date'] = a[18]
			citys.append(dict.copy())
	citys = tuple(citys)

def search_list(value):
	"""
		Функция ищет 'geonameid'
		в списке из словарей и возвращает 
		найденный словарь
	"""
	for i in citys:
		if len(i['geonameid']) != len(value):
			continue
		if i['geonameid'] == value:
			return i
	return None

def search_pages(page, amount_citys):
	"""
		Функция по выводу городов на указанной
		странице и по количеству городов на ней.
	"""
	count_serch =  int(page) * int(amount_citys)
	count = 1
	all_pages = 1
	find_citys = []
	for i in citys:
		if ((count_serch - (int(amount_citys) -1)) <= count and
			count <= count_serch):
			find_citys.append(i)
		count += 1
		all_pages += 1
	return find_citys, ceil((all_pages/int(amount_citys)))

def city_comparison(first_city, second_city):
	"""
		Функция находит 2 города введеных на
		русском языке. находит данные по этим
		городам и сравнивает их данные.
	"""
	population_first = -1
	population_second = -1
	for i in citys:
		for j in i['alternatenames']:
			if first_city == j:
				if population_first < int(i['population']):
					population_first = int(i['population'])
					first_city = i
		for j in i['alternatenames']:
			if second_city == j:
				if population_second < int(i['population']):
					population_second = int(i['population'])
					second_city = i
	return first_city, second_city

def time_zone_search(first_time_zone, second_time_zone):
	"""
		Функция определяет на сколько отличается
		время у первой и второй зоны от гринвича,
		а затем возвращает разницу между ними
	"""
	with open('timeZones.txt', 'r') as time:
		for i in time.read().splitlines():
			a = i.split('\t')
			if first_time_zone == a[1]:
				first_GMT = float(a[3])
			if second_time_zone == a[1]:
				second_GMT = float(a[3])
		return (int(first_GMT - second_GMT) if (first_GMT - second_GMT) > 0
			else int((first_GMT - second_GMT) * (-1)))
