#это тесты
import pytest
import allure
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
@allure.feature('Работа со стеной')
@allure.story('Публикация поста на стене')
def test_wall_post(vk_client):
    """Тест создание  поста на стене"""
    text = {
        'message': 'всем привет'
    }
    with allure.step('Отправляем POST‑запрос на публикацию поста'):
        response = vk_client.wall_post(message=text['message'])

    with allure.step('Проверяем статус‑код ответа'):
        assert response.status_code == 200, f"Ошибка публикации: {response.text}"

    with allure.step('Проверяем отсутствие ошибок в ответе API'):
        result = response.json()
        assert 'error' not in result, f"API вернуло ошибку: {result.get('error')}"


@allure.feature('Работа со стеной')
@allure.story('Публикация постов на стене без текста')
def test_wall_post_negative(vk_client, negative_post_payload):
    """Тест создание  поста на стене без текста """
    with allure.step('Отправляем POST‑запрос с пустым сообщением'):
        response = vk_client.wall_post(message=negative_post_payload['message'])

    with allure.step('Проверяем статус‑код ответа'):
        assert response.status_code == 200, f"Ошибка публикации: {response.text}"
    with allure.step('Проверяем, что API вернуло ошибку из‑за пустого сообщения'):
        result = response.json()

        assert 'error'  in result, f"API не вернуло ошибку: {result.get('error')}"


@allure.feature('Работа с альбомами')
@allure.story('Создание фотоальбома')
def test_create_album(vk_client, album_data):
    """Тест создания альбома для фотографий"""
    with allure.step('Отправляем запрос на создание альбома'):
        response = vk_client.create_album(title=album_data['title'])

    with allure.step('Проверяем статус‑код ответа'):
        assert response.status_code == 200, f"Ошибка создания альбома: {response.text}"

    with allure.step('Проверяем отсутствие ошибок в ответе API'):
        result = response.json()
        assert 'error' not in result, f"API вернуло ошибку: {result.get('error')}"

    with allure.step('Проверяем наличие ID созданного альбома в ответе'):
        assert 'response' in result and 'id' in result['response'], "В ответе отсутствует ID созданного альбома"


@allure.feature('Работа с данными о друзьях')
@allure.story('Поиск данных о друзьях')
def test_friends_search(vk_client):
    """Тест поиска друзей"""
    with allure.step('Отправляем запрос на поиск друзей'):
        response = vk_client.friends_search()

    with allure.step('Проверяем статус‑код ответа'):
        assert response.status_code == 200, f"Ошибка поиска друзей: {response.text}"

    with allure.step('Проверяем отсутствие ошибок в ответе API'):
        result = response.json()
        assert 'error' not in result, f"API вернуло ошибку: {result.get('error')}"



@allure.feature('Работа с альбомами')
@allure.story('Управление фотоальбомами пользователя')
def test_delete_album(vk_client, album_data):
    """Тест удаления альбома: создаём альбом, получаем его ID, затем удаляем"""

    with allure.step('Создаём альбом'):
        create_response = vk_client.create_album(title=album_data['title'])
        assert create_response.status_code == 200, f"Ошибка создания альбома: {create_response.text}"

    with allure.step('Получаем ID созданного альбома и owner_id'):
        create_result = create_response.json()
        assert 'error' not in create_result, f"API вернуло ошибку при создании альбома: {create_result.get('error')}"
        album_id = create_result['response']['id']
        owner_id = create_result['response']['owner_id']  # Берём owner_id из ответа API, а не из app_id

    with allure.step('Шаг 2: Удаляем созданный альбом'):
        delete_response = vk_client.delete_album(album_id=album_id, owner_id=owner_id)
        assert delete_response.status_code == 200, f"Ошибка удаления альбома: {delete_response.text}"

    with allure.step('Дополнительная проверка: убеждаемся, что альбом действительно удалён'):
        delete_result = delete_response.json()
        assert 'error' not in delete_result, f"API вернуло ошибку при удалении альбома: {delete_result.get('error')}"
        assert delete_result.get('response') == 1, "Ответ API не подтверждает удаление альбома (ожидается 1)"




