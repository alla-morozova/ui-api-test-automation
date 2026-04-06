#это тесты
import pytest
from API import VKAPIClient


@pytest.fixture
def vk_client():
    """Фикстура для создания экземпляра клиента VK API"""
    return VKAPIClient()


@pytest.fixture
def negative_post_payload():
    """Фикстура для данных POST‑запроса"""
    return {
        'message': ''
    }

@pytest.fixture
def album_data():
    """Фикстура для данных альбома"""
    return {
        'title': 'Для фотографий'
    }

def test_wall_post(vk_client):
    """Тест создание  поста на стене"""
    text = {
        'message': 'всем привет'
    }
    response = vk_client.wall_post(message=text['message'])
    assert response.status_code == 200, f"Ошибка публикации: {response.text}"
    result = response.json()
    assert 'error' not in result, f"API вернуло ошибку: {result.get('error')}"


def test_wall_post_negative(vk_client, negative_post_payload):
    """Тест создание  поста на стене без текста """
    response = vk_client.wall_post(message=negative_post_payload['message'])
    assert response.status_code == 200, f"Ошибка публикации: {response.text}"
    result = response.json()
    assert 'error'  in result, f"API не вернуло ошибку: {result.get('error')}"


def test_create_album(vk_client, album_data):
    """Тест создания альбома для фотографий"""
    response = vk_client.create_album(title=album_data['title'])
    assert response.status_code == 200, f"Ошибка создания альбома: {response.text}"

    result = response.json()
    assert 'error' not in result, f"API вернуло ошибку: {result.get('error')}"
    assert 'response' in result and 'id' in result['response'], "В ответе отсутствует ID созданного альбома"


def test_friends_search(vk_client):
    """Тест поиска друзей"""
    response = vk_client.friends_search()
    assert response.status_code == 200, f"Ошибка поиска друзей: {response.text}"

    result = response.json()
    assert 'error' not in result, f"API вернуло ошибку: {result.get('error')}"


"""Тест удаления альбома: создаём альбом, получаем его ID, затем удаляем"""
def test_delete_album(vk_client, album_data):
    # Шаг 1: Создаём альбом
    create_response = vk_client.create_album(title=album_data['title'])
    assert create_response.status_code == 200, f"Ошибка создания альбома: {create_response.text}"


    # Получаем ID созданного альбома
    create_result = create_response.json()
    assert 'error' not in create_result, f"API вернуло ошибку при создании альбома: {create_result.get('error')}"
    album_id = create_result['response']['id']

    # Получаем owner_id
    owner_id = vk_client.app_id

    # Шаг 2: Удаляем созданный альбом
    delete_response = vk_client.delete_album(album_id=album_id, owner_id=owner_id)
    assert delete_response.status_code == 200, f"Ошибка удаления альбома: {delete_response.text}"


    # Дополнительная проверка: убеждаемся, что альбом действительно удалён
    delete_result = delete_response.json()
    assert 'error' not in delete_result, f"API вернуло ошибку при удалении альбома: {delete_result.get('error')}"
    assert delete_result.get('response') is True, "Ответ API не подтверждает удаление альбома"


