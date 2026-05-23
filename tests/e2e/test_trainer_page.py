import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from conftest import premium_cleanup

from data.test_trainer_data import TRAINER_ID
from data.payment_data import DAYS, card_number, card_actual, card_cvv, card_name, secure_code
from locators.pokemons_list_locators import PokemonsListLocators
from locators.premium_page_locators import PremiumPageLocators
from locators.trainer_page_locators import TrainerPageLocators
from locators.payment_page_locators import PaymentPageLocators

from pages.pokemons_list_page import PokemonsListPage

@allure.suite("Тесты на покупку и отмену Premium")
@allure.tag("premium")
@allure.tag("e2e")
class TestTrainers:
    @allure.title("Переходим на страницу тренера с главной")
    @allure.description("""
        **Предусловие:** Пользователь авторизован на главной странице Pokémon.

        **Шаги:**
        1. Клик по аватару тренера
        2. Проверка перехода по URL `/trainer/{id}`

        **Ожидаемый результат:** Корректный переход на страницу тренера.
        """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke")
    @allure.tag("navigation")
    @pytest.mark.ui
    def test_go_to_trainer_page(self, driver, user_login):
        pokemons_page = PokemonsListPage(driver)
        pokemons_page.go_to_trainer_page()  # Клик + проверка URL

    @allure.title("Переходим со страницы тренера в раздел покупки Премиума")
    @allure.description("""
        **Предусловие:** Пользователь на странице тренера.

        **Шаги:**
        1. Клик по кнопке "Premium"
        2. Проверка перехода по URL `/premium`

        **Ожидаемый результат:** Открыта форма покупки Premium.
        """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke")
    @allure.tag("navigation")
    @pytest.mark.ui
    def test_go_to_premium_page(self, driver, user_login):
        pokemons_page = PokemonsListPage(driver)  # Инициализируем цепочку страниц
        trainer_page = pokemons_page.go_to_trainer_page()
        premium_page = trainer_page.go_to_premium()  # Переходим на Premium (клик + проверка URL)

    @allure.title("Проверяем активности ачивки «Начало большого пути»")
    @allure.description("""
        **Предусловие:** Пользователь на странице тренера.

        **Шаги:**
        1. Проверка видимости иконки ачивки
        2. Проверка атрибута `active`

        **Ожидаемый результат:** Ачивка «Начало большого пути» активна.
        """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("achievement")
    @allure.tag("trainer")
    @pytest.mark.ui
    def test_check_beginning_icon_achievment(self, driver, user_login):
        # Цепочка: главная → тренер → проверка ачивки
        pokemons_page = PokemonsListPage(driver)
        trainer_page = pokemons_page.go_to_trainer_page()
        # Проверка ачивки в 1 методе
        trainer_page.check_beginning_achievement()

    @allure.title("Покупаем Premium")
    @allure.description("""
        **Предусловие:** Пользователь на Premium странице.

        **Шаги:**
        1. Установка количества дней
        2. Клик "Купить Premium" → форма оплаты
        3. Заполнение данных карты
        4. Ввод 3DS SMS кода
        5. Проверка успешной покупки

        **Ожидаемый результат:** Premium активирован.
        **Cleanup:** `premium_cleanup` fixture.
        """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke")
    @allure.tag("payment")
    @allure.tag("critical-path")
    def test_buy_premium(self, driver, user_login, premium_cleanup):
        # Цепочка страниц
        pokemons_page = PokemonsListPage(driver)
        trainer_page = pokemons_page.go_to_trainer_page()
        premium_page = trainer_page.go_to_premium()
        # Покупка Premium
        premium_page.set_days()
        payment_page = premium_page.buy_premium()
        # Оплата
        payment_page.fill_card_form()
        payment_page.submit_payment()
        payment_page.enter_sms_code()
        # Проверка успеха
        assert payment_page.verify_success()

    @allure.title("Отменяем Premium")
    @allure.description("""
        **Предусловие:** Пользователь на Premium странице.

        **Шаги:**
        1. Клик "Отменить Premium"
        2. Подтверждение отмены
        3. Проверка сообщения об успехе

        **Ожидаемый результат:** Подписка отменена.
        """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke")
    @allure.tag("payment")
    @allure.tag("cleanup")
    def test_cancel_premium(self, driver, user_login):
        # Цепочка до Premium страницы
        pokemons_page = PokemonsListPage(driver)
        trainer_page = pokemons_page.go_to_trainer_page()
        premium_page = trainer_page.go_to_premium()
        assert premium_page.cancel_premium()  # Отмена Premium в 1 методе
