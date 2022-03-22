from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from collections import defaultdict

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_correct_plural_year(years):
    trailing_digit = years % 10 if years >= 20 else years
    if trailing_digit == 1:
        return f'{years} год'
    elif 1 < trailing_digit < 5:
        return f'{years} года'
    else:
        return f'{years} лет'


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

wine_data_excel = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', na_values=None, keep_default_na=False)
wines = wine_data_excel.to_dict('records')

wines_categorized = defaultdict(list)
for wine in wines:
    new_wine = dict()
    for key in wine_data_excel.columns.ravel():
        if key == 'Категория':
            continue
        new_wine[key] = wine[key]
    wines_categorized[wine['Категория']].append(new_wine)

founding_year = 1900
years_since = datetime.now().year - founding_year

rendered_page = template.render(
    categories=wines_categorized.keys(),
    wines_categorized=wines_categorized,
    years_since=get_correct_plural_year(years_since)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
