# этот файл содержит фикстуры, которые подготавливают окружение для тестов
from Page import VKAPIClient  # предполагаемый путь к вашему клиенту Page
import pytest
from selenium import webdriver
from Page.main_page import MainPage
# Константы

TIMEOUT = 10  # таймаут для ожиданий
BASE_URL = "https://api.vk.com/method"  # базовый URL VK Page


@pytest.fixture
def vk_client():
    """Фикстура для создания клиента VK Page"""
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


@pytest.fixture
def driver():
    """Фикстура для инициализации драйвера"""
    driver = webdriver.Chrome()
    driver.get("https://vk.com/id710718559")
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для создания экземпляра MainPage"""
    return MainPage(driver)

