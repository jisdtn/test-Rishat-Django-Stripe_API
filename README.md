# Stripe payment forms test project
## _Django-приложение, которое использует API Stripe для платежей_

[Техническое задание](https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit)

## Особенности

> На странице с товаром есть название, описание товара, цена и кнопка 'Buy'. 
>
> При нажатии создается Stripe Session Id для оплаты. 
> 
> Далее - редирект на checkout.stripe.com, где пользователь вводит платежные данные и кликает 'Pay'.
> После успешной транзакции пользователь попадает на страницу Success.


## Стэк

- Python 3.10
- Django 5.0.3
- Stripe 8.8.0
- Requests 2.31.0
- SQLite3
- Docker
- Heroku


## Развернуть проект 
Клонировать репозиторий:

```
git clone https://github.com/jisdtn/test-Rishat-Django-Stripe_API.git
```
В корневой директории проекта 'test-Rishat-Django-Stripe_API' введите команду:

```
make run
```
Помощник запустит оркестрацию docker compose, внутри будут созданы и применены миграции, установлены зависимости и сгенерирован Django secret key.


### Запросы для тестирования

```commandline
http://localhost:8000/item/1
```
```commandline
http://localhost:8000/buy/1
```
```commandline
http://localhost:8000/success/
```

## License

MIT


