# API обмена валют 💱

Проект на FastAPI, который служит простым приложением для обмена валют. 
Пользователи могут получать последние курсы обмена различных валют и выполнять конвертацию валют. 
Проект должен включать аутентификацию JWT для доступа пользователей и интеграцию с открытым API обменных курсов для 
получения данных об обменных курсах в режиме реального времени.


## Технологии ⚙️
* *Python* 
* *FastAPI*
* *Pydantic*
* *JWT*
* *Pytest*


## Запуск  ▶️
1. Клонировать проект на свою локальную машину:


    `git clone https://github.com/Sura1096/Currency_exchange_API.git`

или


    `git clone git@github.com:Sura1096/Currency_exchange_API.git`

2. Находясь в папке проекта:


* Создать для проекта виртуальное окружение:


    `python3.11 -m venv venv`
* Активация виртуального окружения на macOS и Ubuntu:


    `source venv/bin/activate`
* Выйти из виртуального окружения:


    `deactivate`

3. В корне проекта создать файл *.env* и заполнить как в файле *.env.example*


4. Запуск проекта через файл main.py


## API endpoints 🔗

### Регистрация пользователя

* **Endpoint:** `/auth/register/`
* **Метод:** `POST`
* **Тело запроса:**

    
    `{ "username": "example", "password": "password" }`

* **Ответ:**


    `{'message': 'User <USERNAME> successfully added!'}`

### Аутентификация пользователя

* **Endpoint:** `/auth/login/`
* **Метод:** `POST`
* **Тело запроса:**

    
    `{ "username": "example", "password": "password" }`

* **Ответ:**


    `<USER_TOKEN>`

### Список поддерживаемых валют и их кодов

* **Endpoint:** `/currency/list/`
* **Метод:** `GET`
* **Авторизация:** `Bearer <USER_TOKEN>`

* **Ответ:**


    `{ "AED": "United Arab Emirates Dirham", "AMD": "Armenian Dram" }`

### Обмен валюты

* **Endpoint:** `/currency/exchange/`
* **Метод:** `GET`
* **Параметры запроса:**

    
    `{ "from_currency": "USD", "to_currency": "EUR", "amount": 1 }`

* **Авторизация:** `Bearer <USER_TOKEN>`

* **Ответ:**


    `{ "rate": <RESULT> }`

## Внешний API 🤝

- **API:** [Currency Data API](https://apilayer.com/marketplace/currency_data-api)
- **API_URL:** `https://api.apilayer.com/currency_data`


Чтобы использовать этот API, понадобится ключ API, который можно получить 
зарегистрировавшись на сайте. 
Ключ API следует хранить в файле .env, чтобы обеспечить его безопасность.
