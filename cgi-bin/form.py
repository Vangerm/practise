#!/usr/bin/env python3
import cgi
import read

read.download_list()
form = cgi.FieldStorage()
geonameid = read.search_list(form.getfirst("geonameid"))

if geonameid:
	print("Content-type: text/html\n")
	print(f"""<!DOCTYPE HTML>
	        <html>
	        <head>
	            <meta charset="utf-8">
	            <title>{geonameid['name']}</title>
	        </head>
	        <body>""")

	print(f"<h2>{geonameid['name']}</h2>")
	print(f"<p>geonameid: {geonameid['geonameid']} |")
	print(f"name: {geonameid['name']} |")
	print(f"asciiname: {geonameid['asciiname']} |")
	print(f"alternatenames:{geonameid['alternatenames']}</p>")
	print(f"<p>latitude: {geonameid['latitude']} |")
	print(f"longitude: {geonameid['longitude']} |")
	print(f"feature_class: {geonameid['feature_class']} |")
	print(f"feature_code: {geonameid['feature_code']} |")
	print(f"country_code: {geonameid['country_code']} |")
	print(f"cc2: {geonameid['cc2']}</p>")
	print(f"<p>population: {geonameid['population']} |")
	print(f"elevation: {geonameid['elevation']} |")
	print(f"dem: {geonameid['dem']} |")
	print(f"timezone: {geonameid['timezone']} |")
	print(f"modification_date: {geonameid['modification_date']}</p>")
	print("""<div>
			<input type="button" onclick="location.href='../';" value="На главную"/>
		</div>""")

	print("""</body>
	        </html>""")
