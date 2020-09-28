#!/usr/bin/env python3
import cgi
import read

read.download_list()
form = cgi.FieldStorage()

first_city = form.getfirst("first_city")
second_city = form.getfirst("second_city")

first_city, second_city = read.city_comparison(first_city, second_city)

if first_city and second_city:
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
	        <html>
	        <head>
	            <meta charset="utf-8">
	            <title>Поиск</title>
	        </head>
	        <body>""")

	print(f"<p>geonameid: {first_city['geonameid']} |")
	print(f"name: {first_city['name']} |")
	print(f"asciiname: {first_city['asciiname']} |")
	print(f"alternatenames:{first_city['alternatenames']}</p>")
	print(f"<p>latitude: {first_city['latitude']} |")
	print(f"longitude: {first_city['longitude']} |")
	print(f"feature_class: {first_city['feature_class']} |")
	print(f"feature_code: {first_city['feature_code']} |")
	print(f"country_code: {first_city['country_code']} |")
	print(f"cc2: {first_city['cc2']}</p>")
	print(f"<p>population: {first_city['population']} |")
	print(f"elevation: {first_city['elevation']} |")
	print(f"dem: {first_city['dem']} |")
	print(f"timezone: {first_city['timezone']} |")
	print(f"modification_date: {first_city['modification_date']}</p>")
	print("<hr align='left' width='500' size='1'/>")
	print(f"<p>geonameid: {second_city['geonameid']} |")
	print(f"name: {second_city['name']} |")
	print(f"asciiname: {second_city['asciiname']} |")
	print(f"alternatenames:{second_city['alternatenames']}</p>")
	print(f"<p>latitude: {second_city['latitude']} |")
	print(f"longitude: {second_city['longitude']} |")
	print(f"feature_class: {second_city['feature_class']} |")
	print(f"feature_code: {second_city['feature_code']} |")
	print(f"country_code: {second_city['country_code']} |")
	print(f"cc2: {second_city['cc2']}</p>")
	print(f"<p>population: {second_city['population']} |")
	print(f"elevation: {second_city['elevation']} |")
	print(f"dem: {second_city['dem']} |")
	print(f"timezone: {second_city['timezone']} |")
	print(f"modification_date: {second_city['modification_date']}</p>")
	print("<hr align='left' width='500' size='1'/>")
	print("<p>Город севернее: ")
	print(f"{first_city['name']}" if first_city['latitude'] > second_city['latitude'] 
		else f"{second_city['name']}")
	print("</p>")
	print("<p>")
	print("В одной зоне" if first_city['timezone'] == second_city['timezone']
		else "В разных")
	print("</p>")
	print("<p>")
	print(f"""Разница во времени: 
		{read.time_zone_search(first_city['timezone'],second_city['timezone'])}
		&nbsp; часа/часов</p>""")
	print("""<div>
			<input type="button" onclick="location.href='../';" value="На главную"/>
		</div>""")

	print("""</body>
	        </html>""")