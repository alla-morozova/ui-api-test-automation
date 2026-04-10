from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    # Локаторы элементов
    MUSIC_BUTTON = (By.CSS_SELECTOR, "[data-testid='leftmenuitem-label']")
    GAMES_BUTTON = (By.CSS_SELECTOR, "a[href='/games']")
    VIDEO_BUTTON = (By.CSS_SELECTOR, "a[href='//vkvideo.ru']")
    COMMUNITIES_BUTTON = (By.XPATH, "//a[@href='/groups/recommendations']")
    SUBSCRIPTIONS_BUTTON = (By.XPATH, "//*[@title='Подписки']")

    MODAL_TITLE = (By.CSS_SELECTOR, "[data-testid='box_title_text']")
    MODAL_CONTENT = (
        By.XPATH,
        "//*[contains(@class, 'feed') or contains(@class, 'subscription') or contains(@class, 'list')]",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_current_url(self):
        """Получение текущего URL страницы"""
        return self.driver.current_url

    def click_music_button(self):
        """Клик по кнопке «Музыка»"""
        music_button = self.wait.until(
            EC.element_to_be_clickable(self.MUSIC_BUTTON)
        )
        assert (
            music_button.is_displayed()
        ), "Кнопка «Музыка» не отображается на странице"
        music_button.click()
        self.wait.until(EC.url_contains("audio"))

    def click_games_button(self):
        """Клик по кнопке «Игры»"""
        games_button = self.wait.until(
            EC.element_to_be_clickable(self.GAMES_BUTTON)
        )
        assert (
            games_button.is_displayed()
        ), "Кнопка «Игры» не отображается на странице"
        games_button.click()
        self.wait.until(EC.url_contains("games"))

    def click_video_button(self):
        """Клик по кнопке «Видео» (открывает новое окно)"""
        video_button = self.wait.until(
            EC.element_to_be_clickable(self.VIDEO_BUTTON)
        )
        assert (
            video_button.is_displayed()
        ), "Кнопка «Видео» не отображается на странице"

        original_windows_count = len(self.driver.window_handles)
        video_button.click()

        self.wait.until(
            lambda driver: len(driver.window_handles) > original_windows_count
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_contains("vkvideo.ru"))

    def click_communities_button(self):
        """Клик по кнопке «Сообщества»"""
        communities_button = self.wait.until(
            EC.element_to_be_clickable(self.COMMUNITIES_BUTTON)
        )
        assert (
            communities_button.is_displayed()
        ), "Кнопка «Сообщества» не отображается на странице"
        communities_button.click()
        self.wait.until(EC.url_contains("/groups/recommendations"))

    def click_subscriptions_button(self):
        """Клик по кнопке «Подписки»"""
        subscriptions_button = self.wait.until(
            EC.element_to_be_clickable(self.SUBSCRIPTIONS_BUTTON)
        )
        assert (
            subscriptions_button.is_displayed()
        ), "Кнопка «Подписки» не отображается на странице"
        subscriptions_button.click()

        modal_title = self.wait.until(
            EC.visibility_of_element_located(self.MODAL_TITLE)
        )
        assert (
            modal_title.is_displayed()
        ), "Модальное окно «Подписки» не появилось после клика"

        content_element = self.wait.until(
            EC.visibility_of_element_located(self.MODAL_CONTENT)
        )
        assert (
            content_element.is_displayed()
        ), "Контент модального окна подписок не отображается"
