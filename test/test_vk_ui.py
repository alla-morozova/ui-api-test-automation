import allure
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Навигация по VK")
class TestVKNavigation:

    @allure.story("Переход в раздел Музыка")
    def test_click_music_button(self, main_page):
        with allure.step("Клик по кнопке «Музыка» и ожидание перехода"):
            main_page.click_music_button()

        with allure.step("Проверка URL после перехода"):
            current_url = main_page.get_current_url()
            expected_url = "https://vk.com/audio"
            assert (
                current_url == expected_url
            ), f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.story("Переход в раздел Игры")
    def test_click_games_button(self, main_page):
        with allure.step("Клик по кнопке «Игры» и ожидание перехода"):
            main_page.click_games_button()

        with allure.step("Проверка URL после перехода"):
            current_url = main_page.get_current_url()
            expected_url = "https://vk.com/games"
            assert (
                current_url == expected_url
            ), f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.story("Переход в раздел Видео")
    def test_click_video_button(self, main_page):
        with allure.step(
            "Клик по кнопке «Видео» и ожидание открытия нового окна"
        ):
            main_page.click_video_button()

        with allure.step("Проверка URL в новом окне"):
            current_url = main_page.get_current_url().lower()
            assert (
                "vkvideo.ru" in current_url
            ), f"URL не содержит 'vkvideo.ru': {current_url}"
            expected_url = "https://vkvideo.ru/"
            assert (
                current_url == expected_url
            ), f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.story("Переход в раздел Сообщества")
    def test_click_communities_button(self, main_page):
        urlvk = "https://vk.com/groups/recommendations?act=recommendations&c%5Bcategory%5D=0"
        with allure.step("Клик по кнопке «Сообщества» и ожидание перехода"):
            main_page.click_communities_button()

        with allure.step("Проверка URL после перехода"):
            current_url = main_page.get_current_url()
            expected_url = urlvk
            assert (
                current_url == expected_url
            ), f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.story("Открытие модального окна Подписки")
    def test_click_subscriptions_button(self, main_page):
        with allure.step(
            "Клик по кнопке «Подписки» и ожидание модального окна"
        ):
            main_page.click_subscriptions_button()

        with allure.step("Проверка заголовка модального окна"):
            modal_title_element = main_page.wait.until(
                EC.visibility_of_element_located(main_page.MODAL_TITLE)
            )
            actual_title_text = modal_title_element.text.strip()
            assert actual_title_text.startswith(
                "Подписки"
            ), f"Заголовок не начинается с 'Подписки'. Получен: '{actual_title_text}'"

        with allure.step("Проверка контента модального окна"):
            content_element = main_page.wait.until(
                EC.visibility_of_element_located(main_page.MODAL_CONTENT)
            )
            assert (
                content_element.is_displayed()
            ), "Контент модального окна подписок не отображается"
