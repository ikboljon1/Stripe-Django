# Django Stripe.


Тестовое задание для одной из компаний. Простой магазин Django с Stripe.
Основная цель состоит в том, чтобы иметь конечную точку `/item/<item_id>`, которая будет возвращать HTML с информацией об элементе (из базы данных сервера) и кнопкой покупки,
который выберет другой маршрут (API) (`/buy/<item_id>`), который вернет идентификатор сеанса Stripe, который используется для перенаправления пользователя на экран оплаты (фактически, сам Stripe).


## Методы.

[`/item/<id>`](http://localhost:8000/tests/stripe/item/): возвращает HTML-страницу с информацией о предмете и кнопкой для покупки выбранного предмета. \
[`/buy/<id>`](http://localhost:8000/tests/stripe/buy/): возвращает идентификатор сеанса Stripe (на самом деле страница элемента выбирает эту конечную точку для перенаправления самостоятельно). \
[`/admin/*`](http://localhost:8000/tests/stripe/admin/): Проект поддерживает Django-Admin для работы с моделями (Предметы, Скидки и т.д.). \
[`/`](http://localhost:8000/tests/stripe/): Простая индексная страница.

## Как запустить?

Проект использует Docker, для запуска просто сделайте это в корне репозитория:
`cd src && docker-compose up`. Это запустит Docker, базу данных и сервер с Gunicorn с рабочими Uvicorn!
#### Статические файлы?
В настоящее время статические файлы обслуживаются Ngninx (+Django `collectstatic`)
При разработке статические файлы доступны только при использовании django `runserver`
#### Миграции?
Запустите `docker exec -it django-stripe-server-1 /bin/sh`, а затем `python manage.py makemigrations && python manage.py migrate`, это вызовет миграцию всех баз данных!
## Как настроить?

Вы можете изменить переменные среды внутри файла `/src/.server.env`, который будет передан на сервер с помощью Docker. Посмотрите главы Django/App.
STRIPE_API_PUBLISHABLE_KEY, STRIPE_API_SECRET_KEY — это ключи Stripe, которые можно найти [здесь] (https://dashboard.stripe.com/test/dashboard).
`URL_PREFIX` используется только для URL-адресов под прокси. Все остальные настройки относятся к полям Django по умолчанию.
## Технологии.

- Python / Django (без DRF, потому что основная цель не в том, чтобы сделать API).
- Gunicorn с рабочими Uvicorn (ASGI).
- Stripe API для платежей.
- Докер / Docker-Compose
- PostgreSQL (с PgBouncer)/Django ORM
- Рабочие процессы GitHub (CI/CD)
- Nginx на стороне сервера в качестве прокси-сервера.
- Ubuntu в качестве серверной ОС.

## CI / CD.

- CD: проект имеет рабочий процесс развертывания, который автоматически развертывает все изменения, отправленные в «основную» ветку.
- CI: у проекта есть рабочий процесс тестов, который будет запускать тесты Django / Test Docker, когда вы объединяете ветку с основной веткой.
   На данный момент для этого проекта не написаны специальные тесты, поэтому тесты не так уж и полезны.

## Тестирование.
Запустите `docker exec -it django-stripe-server-1 /bin/sh`, а затем `python manage.py test`, это запустит все тесты!

