#!/usr/bin/env python3
import cgi
import read

read.download_list()
form = cgi.FieldStorage()

page = form.getfirst("page")
amount_citys = form.getfirst("amount_citys")

find_citys, all_pages = read.search_pages(page, amount_citys)

if find_citys:
	print("Content-type: text/html\n")
	print(f"""<!DOCTYPE HTML>
	        <html>
	        <head>
	            <meta charset="utf-8">
	            <title>Страница {page}</title>
	        </head>
	        <body>""")

	for i in find_citys:
		print(f"<p>geonameid: {i['geonameid']} |")
		print(f"name: {i['name']} |")
		print(f"asciiname: {i['asciiname']} |")
		print(f"alternatenames:{i['alternatenames']}</p>")
		print(f"<p>latitude: {i['latitude']} |")
		print(f"longitude: {i['longitude']} |")
		print(f"feature_class: {i['feature_class']} |")
		print(f"feature_code: {i['feature_code']} |")
		print(f"country_code: {i['country_code']} |")
		print(f"cc2: {i['cc2']}</p>")
		print(f"<p>population: {i['population']} |")
		print(f"elevation: {i['elevation']} |")
		print(f"dem: {i['dem']} |")
		print(f"timezone: {i['timezone']} |")
		print(f"modification_date: {i['modification_date']}</p>")
		print("<hr align='left' width='500' size='1'/>")
	print("<div><table><tr>")
	if int(page) > 1:
		print(f"""<th><form action="form_second.py">
				<input type="hidden" name="page" value="1">
				<input type="hidden" name="amount_citys" value="{amount_citys}">
				<input type="submit" value="1"/>
			</form></th>""")
	if int(page) > 4:
		print("<th>...</th>")
	if int(page) > 3:
		print(f"""<th><form action="form_second.py">
				<input type="hidden" name="page" value="{int(page)-2}">
				<input type="hidden" name="amount_citys" value="{amount_citys}">
				<input type="submit" value="{int(page)-2}"/>
			</form></th>""")
	if int(page) > 2:
		print(f"""<th><form action="form_second.py">
				<input type="hidden" name="page" value="{int(page)-1}">
				<input type="hidden" name="amount_citys" value="{amount_citys}">
				<input type="submit" value="{int(page)-1}"/>
			</form></th>""")
	print(f'<th>{page}</th>')
	if int(page) < all_pages:
		print(f"""<th><form action="form_second.py">
					<input type="hidden" name="page" value="{int(page)+1}">
					<input type="hidden" name="amount_citys" value="{amount_citys}">
					<input type="submit" value="{int(page)+1}"/>
				</form></th>""")
	if int(page) < all_pages -1:
		print(f"""<th><form action="form_second.py">
				<input type="hidden" name="page" value="{int(page)+2}">
				<input type="hidden" name="amount_citys" value="{amount_citys}">
				<input type="submit" value="{int(page)+2}"/>
			</form></th>""")
	if int(page) < all_pages -2:
		print(f"""<th>...</th>
				<th><form action="form_second.py">
					<input type="hidden" name="page" value="{all_pages}">
					<input type="hidden" name="amount_citys" value="{amount_citys}">
					<input type="submit" value="{all_pages}"/>
				</form></th>""")
	print("</tr></table></div>")
	print("""<div>
			<input type="button" onclick="history.back();" value="Назад"/>
			<input type="button" onclick="location.href='../';" value="На главную"/>
		</div>""")

	print("""</body>
	        </html>""")