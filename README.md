# Бары.

Данный скрипт показывает самый большой бар, самый маленький бар и самый ближайший бар (*данные нужно ввести с клавиатуры при запросе*)

Для работы нужен файл в формате **json**, его можно получить на [этой](http://data.mos.ru/opendata/7710881420-bary "список московских баров") странице, кликнув **Скачать** и выбрав пункт **json** или по [прямой ссылке](http://data.mos.ru/opendata/export/1796/json/2/1).

## Запуск скрипта.

Для получения справки нужно запустить скрипт с флагом `-h` или `--help`
Для запуска вводим:

```python
python3 bars.py Бары.json
```
Пример работы скрипта:

```python
python3 bars.py Бары.json
Самый большой бар: Ночной клуб «Орфей»
Самый маленький бар: БАР В ГОСТИНИЦЕ
Введите ваши координаты:
Долгота: 37.6173
Широта: 55.7558
Самый близкий бар: Бар столовой № 1
``` 
