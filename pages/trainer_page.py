from data.test_trainer_data import TRAINER_ID
from locators.trainer_page_locators import TrainerPageLocators
from pages.base_page import BasePage
from locators.premium_page_locators import PremiumPageLocators
import time

class TrainerPage(BasePage):
    PREMIUM_URL = "https://pokemonbattle.ru/premium"
    TRAINER_URL = f"https://pokemonbattle.ru/trainer/{TRAINER_ID}"

    def go_to_premium(self):
        """Переход в раздел покупки Premium"""
        self.click(TrainerPageLocators.premium_button)  # Кликаем кнопку Premium
        self.wait.until(lambda d: "/premium" in d.current_url)  # Ждём и проверяем URL Premium страницы
        assert self.driver.current_url == self.PREMIUM_URL, f"Ожидали {self.PREMIUM_URL}, получили {self.driver.current_url}"
        # Возвращаем PremiumPage
        from pages.premium_page import PremiumPage
        return PremiumPage(self.driver)

    def check_beginning_achievement(self):
        """Проверяет активность ачивки «Начало большого пути»"""
        assert self.driver.current_url == self.TRAINER_URL  # Проверяем, что мы на странице тренера
        achievement = self.find(PremiumPageLocators.BEGINNING_ACHIEVEMENT_ACTIVE)  # Находим и проверяем активную ачивку
        assert achievement.is_displayed(), "Ачивка 'Начало большого пути' не активна!"
        return True

    def should_be_loaded(self):
        self.element_visible(TrainerPageLocators.TRAINER_CARD)
        time.sleep(1)

    def hide_element(self, locator):
        """Скрывает элемент по локатору через JS"""
        try:
            element = self.find(locator)
            self.driver.execute_script("arguments[0].style.display = 'none'; arguments[0].style.visibility = 'hidden';", element)
        except:
            pass  # Элемент не найден = ок

    def hide_elements(self, *locators):
        """Скрывает МНОГО элементов одной строкой"""
        for locator in locators:
            try:
                element = self.find(locator)
                self.driver.execute_script("arguments[0].style.display = 'none';", element)
            except:
                pass  # Элемент не найден = ок
        return self
