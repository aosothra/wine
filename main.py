from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from collections import defaultdict

import configargparse
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


def get_arranged_products(excel_filepath):
    products = (pandas.read_excel(
                        excel_filepath,
                        na_values=None,
                        keep_default_na=False).to_dict('records'))

    arranged_products = defaultdict(list)

    for product in products:
        arranged_products[product.pop('Категория')].append(product)

    return arranged_products


def main():
    parser = configargparse.ArgParser(default_config_files=['config.ini'])

    parser.set_defaults(http_ip='0.0.0.0', http_port=8000)
    parser.add_argument('--http_ip', help='IP address of the server')
    parser.add_argument('--http_port', type=int, help='Port of the server')
    parser.add_argument('--index_template', required=True, help='HTML template file to render')
    parser.add_argument('--products_excel', required=True, help='Excel spreadsheet with product listing')
    parser.add_argument('-c', '--config', is_config_file=True, help='Custom config file')

    args = parser.parse_args()

    products = get_arranged_products(args.products_excel)

    founding_year = 1920
    winery_age = datetime.now().year - founding_year

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template(args.index_template)

    rendered_page = template.render(
        products=products,
        years_since=get_correct_plural_year(winery_age)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer((args.http_ip, args.http_port), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
