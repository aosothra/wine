# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Настройка

Перед запуском сайта убедитесь, что у вас установлены требуемые зависимости. Для их установки используйте команду:

```
pip install -r requirements.txt
```

Для работы сайта требуется наличие `.xlsx` файла со списком продукции винодельни. На первом листе ожидается таблица следующего содержания (представлено в качестве примера для заполнения):

| Категория | Название | Сорт | Цена | Картинка | Акция |
| --------- | -------- | ---- | ---- | -------- | ----- |
| Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение |
| Напитки | Коньяк классический | | 350 | konyak_klassicheskyi.png | |	
| Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png | |
| Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png | |
| Красные вина | Хванчкара | Александраули | 550 | hvanchkara.png | |
| Белые вина | Кокур | Кокур | 450 | kokur.png | |

Вина с одинаковой категорией будут объединены в группы на странице сайта.

Картинки по названиям в поле *Картинка* будут браться из папки `./images/`.

Если поле *Акция* не пустое, то данный товар будет отображаться как акционный. 

Для загрузки файла продукции требуется указать его местоположение в файле конфигурации. По умолчанию, файл конфигурации `config.ini` ожидается в корневом каталоге.

Ниже представлен пример содержания файла конфигурации `config.ini`:

```ini
;Specify PATH to your product spreadsheet
;this parameter must be specified either in here or as an argument --products_excel on start-up
products_excel = './path/to/your/spreadsheet.xlsx'

;Specify PATH to your rendering template for index.html
;original template is distributed as part of the repository. Change it only if template is intentionally relocated.
;this parameter must be specified either in here or as an argument --index_template on start-up
index_template = 'template.html'

;Specify IP address of your HTTP Server from where the rendered page will be served
;This parameter is optional, default value is '0.0.0.0'
;http_ip = '0.0.0.0'

;Specify PORT of your HTTP Server from where the rendered page will be served
;This parameter is optional, default value is 8000
;http_port = 8000
```

Обратите внимание, что помимо пути к файлу продукции в конфигурации также указывается путь к HTML шаблону главной страницы. 

Данный шаблон уже имеется в составе репозитория и находится в корневой папке.

## Запуск

Запустите сайт командой:

```
python main.py
```

В случае если у вас отсутствует файл `config.ini`, переменные путей необходимо указать в качестве параметров:

```
python main.py --products_excel './path/to/your/spreadsheet.xlsx' --index_template './path/to/your/template.html'
```

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
