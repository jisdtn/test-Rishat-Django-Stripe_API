# Stripe payment forms test project
## _Django-приложение, которое использует API Stripe для платежей_

[Ссылка на развернутый проект](https://test-stripe-api-077caba915c4.herokuapp.com/item/1/)

[Техническое задание](https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit)

## Особенности

> На странице с товаром есть название, описание товара,  
> цена и кнопка 'Buy'. 
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


## Подготовить и развернуть проект 
Клонировать репозиторий:

```
git clone https://github.com/jisdtn/test-Rishat-Django-Stripe_API.git
```
Перед тем, как развернуть проект, нужно сгенерировать Django Secret Key.
В корневой директории проекта 'test-Rishat-Django-Stripe_API' введите команду:

```commandline
 bash get_random_secret_key.sh 
```
Вывод должен быть таким: 

```commandline
Created .env
Added SECRET_KEY to .env
```
В файле .env.example вы найдете инструкцию,  
как сгенерировать и куда положить секретный и публичный ключи  
для API Stripe.  

Когда ключи добавлены, нужно развернуть проект командой:

```
make run
```
Помощник запустит оркестрацию docker compose,  
внутри будут созданы и применены миграции и установлены зависимости.

Чтобы проверить проект локально, нужно создать суперпользователя:

```commandline
docker exec -it payment_forms python3 payment_forms/manage.py createsuperuser
```
Перейти в админ-панель и ввести только что присвоенный логин и пароль:

```commandline
http://localhost:8000/admin
```

В админ-панели в модели Item можно создать 1 экземпляр,  
чтобы можно было протестировать урлы ниже: 

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


