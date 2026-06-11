# API автотесты для Restful Booker

Фреймворк для автоматизации API-тестирования сервиса Restful Booker: https://restful-booker.herokuapp.com/

## Используемый стек

* Python 3.14
* pytest
* requests
* Pydantic
* Faker
* python-dotenv
* Allure Report

## Запуск тестов в Docker

```commandline
docker compose run --rm tests
docker compose up allure -d
```

Затем перейти на http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html

## Структура проекта

```text
.
├── assertions/
├── clients/
├── config/
├── models/
├── tests/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Описание директорий

* `assertions/` — переиспользуемые проверки.
* `clients/` — API-клиенты для работы с эндпоинтами.
* `config/` — настройки проекта и работа с переменными окружения.
* `models/` — Pydantic-модели для валидации запросов и ответов.
* `tests/` — набор API-тестов.
* `utils/` — вспомогательные функции и генерация тестовых данных.
* `conftest.py` — фикстуры pytest.
* `pytest.ini` — конфигурация pytest и описание маркеров.

## Настройка окружения

В корне проекта необходимо создать файл `.env`:

```env
BASE_URL=https://restful-booker.herokuapp.com
USERNAME=admin
PASSWORD=password123
TIMEOUT=10
```

Пример шаблона (`.env.example`):

```env
BASE_URL=
USERNAME=
PASSWORD=
TIMEOUT=10
```

## Установка проекта

Клонировать репозиторий:

```bash
git clone <ссылка_на_репозиторий>
cd otus-restful-booker
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение.

Для macOS/Linux:

```bash
source .venv/bin/activate
```

Для Windows:

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск тестов по маркеру:

```bash
pytest -m create_booking
```

Примеры:

```bash
pytest -m get_booking_id
pytest -m get_booking_by_id
pytest -m create_booking
pytest -m update_booking
pytest -m partial_update_booking
pytest -m delete_booking
```

## Формирование Allure-отчёта

Установка Allure (macOS):

```bash
brew install allure
```

Открытие отчёта:

```bash
allure serve allure-results
```

Генерация статического отчёта:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```