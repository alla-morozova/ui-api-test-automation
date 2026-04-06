# этот файл содержит фикстуры, которые подготавливают окружение для тестов
import pytest
from API import VKAPIClient  # предполагаемый путь к вашему клиенту API

# Константы
TIMEOUT = 10  # таймаут для ожиданий
BASE_URL = "https://api.vk.com/method"  # базовый URL VK API

@pytest.fixture
def vk_client():
    """Фикстура для создания клиента VK API"""
    # Здесь можно подгрузить токен из .env или конфигурации
    access_token = "ваш_токен"  # замените на реальный или способ его получения
    client = VKAPIClient(access_token=access_token, base_url=BASE_URL)
    return client

@pytest.fixture
def post_payload():
    """Фикстура с тестовыми данными для публикации поста"""
    return {"message": "Тестовый пост от pytest"}

@pytest.fixture
def album_data():
    """Фикстура с тестовыми данными для создания альбома"""
    return {"title": "Тестовый альбом от pytest"}

()