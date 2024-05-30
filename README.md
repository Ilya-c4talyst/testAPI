# Тестовое задание

Использовались следующие технологии: 

- FastAPI
- pytest

Django для этой задачи, действительно, очень громоздкий :)

## Примеры запросов

На эндпоинт "/" (http://127.0.0.1:8000/) отправляется POST-запрос со следующими данными (JSON):

```plaintext
- date | String | "dd.mm.YYYY" | Дата заявки
- periods | Integer | >= 1 && <= 60 | Количество месяцев по вкладу
- amount | Integer | >= 10_000 && <= 3_000_000 | Сумма вклада
- rate | Float | >= 1 && <= 8 | Процент по вкладу
```

Пример:

```plaintext
{
    "date": "01.05.2021",
    "periods": 5,
    "amount": 100000,
    "rate": 3.6
}
```

Результат - рассчет депозита(JSON). Возвращаются пары дата:ожидаемая сумма, в количестве, равном periods.

```plaintext
{
    "01.05.2021": 100300.0,
    "31.05.2021": 100600.9,
    "30.06.2021": 100902.7,
    "31.07.2021": 101205.41,
    "31.08.2021": 101509.03
}
```

При невалидном запросе возвращается код 400 и сообщение об ошибке.

```plaintext
{
    "date": "01.05.2021",
    "periods": 0,
    "amount": 100000,
    "rate": 3.6
}
```

```plaintext
{
    "error": "periods should be greater than or equal to 1"
}
```

* Можно было создать кастомную валидацию для всех полей, но в ТЗ такого не требовалось.


## Запуск

1. Склонировать репозиторий
2. Создать виртуальное окружение и активировать его
```plaintext
python3 -m venv venv
source venv/bin/activate
```
3. Установить зависимости
```plaintext
pip install -r requirements.txt
```
4. Запустить файл main.py

** Также в /app присутствует Dockerfile для сборки проекта. В ТЗ не было указаний, нужно ли использовать gunicorn, поэтому на данный момент там поле:
```plaintext
CMD ["uvicorn", "main:app", "--host", "127.0.0.0", "--port", "8000"]
```

