# это класс
import os
import json
import requests
from dotenv import load_dotenv
import allure

class VKAPIClient:
    def __init__(self, config_path="config/env_variables.json"):
        load_dotenv()  # Загружаем переменные из .env (если нужны)
        self._load_config(config_path)

    def _load_config(self, config_path):
        """Загрузка переменных из защищённой папки"""
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")

        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # Загружаем переменные из JSON
        self.access_token = config.get("ACCESS_TOKEN")
        self.v = config.get("V")
        self.app_id = config.get("APP_ID")
        self.vk_token_1 = config.get("VK_TOKEN_1")

        # Если переменных нет в JSON, пытаемся взять из .env
        if not self.access_token:
            self.access_token = os.getenv("ACCESS_TOKEN")
        if not self.v:
            self.v = os.getenv("V")
        if not self.app_id:
            self.app_id = os.getenv("APP_ID")
        if not self.vk_token_1:
            self.vk_token_1 = os.getenv("VK_TOKEN_1")

    def _make_request(self, method, url, **kwargs):
        """Базовый метод для выполнения запросов"""
        response = requests.post(url, **kwargs)
        print(f"Метод: {method}")
        print(f"URL: {url}")
        print(f"Статус-код: {response.status_code}")
        print(f"Ответ сервера: {response.text}")
        return response


    def wall_post(self, message="всем привет"):
        """Публикация на стене"""
        url = "https://api.vk.com/method/wall.post"
        payload = {
            'access_token': self.access_token,  # заменили vk_token_1 на access_token
            'v': self.v,
            'message': message
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return self._make_request('POST', url, data=payload, headers=headers)

    def search_hints(self, query="Ольга Зенкина"):
        """Поиск подсказок"""
        url = "https://api.vk.ru/method/search.getHints"
        params = {
            'v': self.v,
            'access_token': self.access_token,
            'q': query
        }
        return self._make_request('POST', url, params=params)

    def create_album(self, title="Для фотографий"):
        """Создание альбома"""
        url = "https://api.vk.ru/method/photos.createAlbum"
        params = {
            'v': self.v,
            'access_token': self.access_token,
            'client_id': self.app_id,
            'title': title
        }
        return self._make_request('POST', url, params=params)

    def friends_search(self, offset=0, count=10):
        """Поиск друзей"""
        url = "https://api.vk.ru/method/friends.search"
        params = {
            'v': self.v,
            'access_token': self.access_token,
            'client_id': self.app_id,
            'fields': "id, first_name, last_name",
            'q': None,
            'offset': str(offset),
            'count': str(count)
        }
        return self._make_request('POST', url, params=params)

    def delete_album(self, album_id, owner_id):
        """Удаление альбома"""
        url = "https://api.vk.ru/method/photos.deleteAlbum"
        params = {
            'v': self.v,
            'access_token': self.access_token,
            'client_id': self.app_id,
            'album_id': str(album_id),
            'owner_id': str(owner_id)
        }
        return self._make_request('POST', url, params=params)