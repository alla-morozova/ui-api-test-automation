# Дипломный проект: Автоматизация тестирования ВКонтакте
ВКонтакте (VK) — крупнейшая социальная сеть в России и странах СНГ.

## Описание проекта
### Проект по автоматизации тестирования сайта ВКонтакте с использованием:

- Python - язык программирования

- Pytest - фреймворк для тестирования;

- Selenium WebDriver - для UI тестов

- Requests - для API тестов

- Allure - для отчетов

Требования
- Python 3.13+

- Google Chrome (последняя версия)

- Git

### Установка и настройка
#### Клонирование репозитория
bash

    ```bash
    git clone <URL-репозиторий>
    ui-api-test-automation cd.

#### Создание виртуального окружения

    ```bash
    python -m venv venv

#### Активация виртуального окружения
Windows:


    ```bash
    venv\Scripts\activate

#### Установка зависимостей

    ```bash
    pip install -r requirements.txt
    requests>=2.31.0
    pytest>=9.0.2
    pytest-html>=4.1.1
    allure-pytest>=2.15.3
    flake8>=6.1.0
    selenium==4.41.0
    webdriver-manager==4.0.2
    pytest-repeat==0.9.4
    python-dotenv==1.2.2



#### Настройка переменных окружения
Скопируйте env_variables.json и заполните необходимые значения:
    "APP_ID"=ваш_app_id (из аккаунта на странице аутентификации)
    ACCESS_TOKEN=ваш_access_token(посмотреть инструменты разработчика (F12))

Скопируйте .env и заполните необходимые значения:

V=5.199
BASE_URL=https://api.vk.com
SEARCH_BASE_URL=https://api.vk.ru

#### Команды для запуска тестов
Все тесты (UI + API):
bash
pytest 

Только API тесты
bash
pytest -m api -v

Только UI тесты
bash
pytest -m ui -v

Запуск с Allure отчетом
bash
pytest --alluredir=allure-results -v
allure serve allure-results

Параллельный запуск тестов
bash
pytest -n auto -v

Запуск конкретного тестового файла
bash
pytest tests/test1_api.py -v
pytest tests/test_vk_ui.py -v

Запуск конкретного теста по имени
bash
pytest -k "название файла" -v 

### Ссылка на финальный проект:
https://morozova-.yonote.ru/share/e82960e8-5597-4806-9c03-d4a47192e383

### Тип тестов Кол-во Результат

API тесты 5 Все пройдены
UI тесты 5 Все пройдены

Общее покрытие 10 - 100% успешно

### Структура проекта: 
ui-api-test-automation/

├── config/

│ └── env_variables.json # Пример переменных окружения

├──Page/

│ └── api1.py  # Базовый Page Object

│ └── main_page.py # Базовый Page Object

├── test/

│ ├── test1_api.py # API тесты (5 шт.)

│ ├── test_vk_ui.py # UI тесты (5 шт.)

│ └── conftest.py # Фикстуры для тестов

├── .env # Пример переменных окружения

├── .gitignore # Игнорируемые файлы

├── pytest.ini # Конфигурация pytest

├── requirements.txt # Зависимости проекта

└── README.md # Документация

### Что автоматизировано

API тесты (5 тестов): 

test_wall_post - создание поста на стене

test_wall_post_negative - создание поста на стене без текста

test_create_album - создание альбома для фотографий

test_friends_search - поиск данных о друзьях(10чел)

test_delete_album- удаление альбома: создаём альбом, получаем его ID, затем удаляем


UI тесты (5 тестов):

test_click_music_button - проверка работы перехода в раздел "Музыка" (проверка правильности URL: `https://vk.com/audio)

test_click_games_button - проверка работы перехода в раздел "Игры" (проверка правильности URL: `https://vk.com/ games`)

test_click_video_button - проверка работы перехода в раздел Видео (проверка URL в новом окне: https://vkvideo.ru/)

test_click_communities_button - проверка перехода в раздел "Сообщества" (проверка URL)

test_click_subscriptions_button - проверка перехода в раздел "Подписки" (проверка открытия модального окна, заголовок начинается с 'Подписки')


### Автор

Морозова Алла - Дипломный проект по автоматизации тестирования

### Дата

10 апреля 2026 г.

Если что‑то не работает или нужны пояснения, пишите мне:
 Telegram: @Alla_Morozova1
 Email: alla.morozova@mail.ru