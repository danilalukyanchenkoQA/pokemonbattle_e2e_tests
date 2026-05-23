import time
import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.payment_data import VALID_CARD, INVALID_CARD_NUMBER, INVALID_EXPIRY, card_name, card_cvv, card_number, card_actual
from locators.payment_page_locators import PaymentPageLocators
from locators.premium_page_locators import PremiumPageLocators
from locators.trainer_page_locators import TrainerPageLocators
from pages.pokemons_list_page import PokemonsListPage

class TestScreenshot:
    @allure.title("Карточка тренера")
    @allure.tag("trainer", "screenshot", "card")
    @allure.description("Проверяет вёрстку карточки тренера без достижений, уровня и покеболов")
    def test_trainer_card(self, driver, user_login, assert_snapshot):
        pokemons_page = PokemonsListPage(driver)
        trainer_page = pokemons_page.go_to_trainer_page()
        trainer_page.should_be_loaded()
        trainer_page.hide_elements(
            TrainerPageLocators.ACHIEVEMENTS,
            TrainerPageLocators.LEVEL_NUMBER,
            TrainerPageLocators.POKEBALLS
        )
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located(TrainerPageLocators.ACHIEVEMENTS))
        wait.until(EC.invisibility_of_element_located(TrainerPageLocators.LEVEL_NUMBER))
        wait.until(EC.invisibility_of_element_located(TrainerPageLocators.POKEBALLS))

        screenshot = trainer_page.find(TrainerPageLocators.TRAINER_CARD).screenshot_as_png
        assert_snapshot(screenshot, name="trainer_card.png", threshold=0.05)

    @allure.title("Премиум: стоимость за {days} дней")
    @allure.tag("premium", "screenshot", "cost")
    @allure.description("Проверяет отображение стоимости премиума для разных периодов")
    @pytest.mark.parametrize("days", [15, 90, 250, 400], ids=["до30", "30-180", "180-365", ">365"])
    def test_premium_page_days(self, driver, user_login, assert_snapshot, days):
        pokemons_page = PokemonsListPage(driver)
        trainer_page = pokemons_page.go_to_trainer_page()
        premium_page = trainer_page.go_to_premium()
        premium_page.set_days(days)
        screenshot = premium_page.find(PremiumPageLocators.COST_DAYS).screenshot_as_png
        assert_snapshot(screenshot, name=f"premium_cost_{days}_days.png", threshold=0.05)

    @allure.title("Форма оплаты: {scenario}")
    @allure.tag("payment", "screenshot", "form")
    @allure.description("Проверяет вёрстку формы оплаты в разных состояниях")
    @pytest.mark.parametrize("scenario, card_data", [
        pytest.param("empty form", {}, id="empty_form"),
        pytest.param("valid form", VALID_CARD, id="valid_form"),
        pytest.param("wrong card number", {
            "number": INVALID_CARD_NUMBER,
            "expiry": card_actual,
            "cvv": card_cvv,
            "name": card_name
        }, id="invalid_card"),
        pytest.param("invalid card date", {
            "number": card_number,
            "expiry": INVALID_EXPIRY,
            "cvv": card_cvv,
            "name": card_name
        }, id="invalid_expiry"),
    ])
    def test_payment_form_states(self, navigate_to_payment, assert_snapshot, scenario, card_data):
        payment_page = navigate_to_payment

        if card_data:
            payment_page.fill_card_partial(card_data)

        wait = WebDriverWait(payment_page.driver, 10)
        wait.until(EC.visibility_of_element_located(PaymentPageLocators.PAYMENT_FORM))
        screenshot = payment_page.find(PaymentPageLocators.PAYMENT_FORM).screenshot_as_png
        assert_snapshot(screenshot, name=f"payment_{scenario}.png", threshold=0.05)
