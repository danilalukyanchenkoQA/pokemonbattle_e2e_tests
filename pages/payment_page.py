from pages.base_page import BasePage
from locators.payment_page_locators import PaymentPageLocators
from data.payment_data import card_number, card_actual, card_cvv, card_name, secure_code

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PaymentPage(BasePage):
    THREEDS_URL_PATTERN = "/payment_3ds"

    def fill_card_form(self):
        """Заполняет все поля карты"""
        # Номер карты
        card_input = self.find(PaymentPageLocators.CARD_NUMBER)
        self.driver.execute_script("arguments[0].value = arguments[1];", card_input, card_number)
        assert card_input.get_attribute("value") == card_number

        # Срок действия
        self.type(PaymentPageLocators.CARD_ACTUAL, card_actual)

        # CVV
        self.type(PaymentPageLocators.CSV_INPUT, card_cvv)

        # Имя держателя
        name_input = self.find(PaymentPageLocators.NAME_INPUT)
        self.driver.execute_script("arguments[0].value = arguments[1];", name_input, card_name)
        assert name_input.get_attribute("value") == card_name

    def submit_payment(self):
        """Отправляет платёж → 3DS"""
        self.click(PaymentPageLocators.PAY_BUTTON)
        self.wait.until(lambda d: self.THREEDS_URL_PATTERN in d.current_url)
        assert self.THREEDS_URL_PATTERN in self.driver.current_url

    def enter_sms_code(self):
        """Вводит SMS код"""
        self.type(PaymentPageLocators.SMS_CODE_INPUT, secure_code)
        self.click(PaymentPageLocators.SEND_CODE_BUTTON)

    def verify_success(self):
        """Проверяет успешную покупку"""
        success_title = self.find(PaymentPageLocators.SUCCESS_TITLE)
        assert success_title.text.strip() == "Покупка прошла успешно"
        return True

    def fill_card_partial(self, card_data):
        """Частичное заполнение формы"""
        if "number" in card_data:
            self.set_field(PaymentPageLocators.CARD_NUMBER, card_data["number"])
        if "expiry" in card_data:
            self.type(PaymentPageLocators.CARD_ACTUAL, card_data["expiry"])
        if "cvv" in card_data:
            self.type(PaymentPageLocators.CSV_INPUT, card_data["cvv"])
        if "name" in card_data:
            self.set_field(PaymentPageLocators.NAME_INPUT, card_data["name"])

    def set_field(self, locator, value):
        """Универсальная установка значения"""
        field = self.find(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", field, value)

    def wait_error_visible(self, error_locator):
        self.wait.until(EC.visibility_of_element_located(error_locator))

    def wait_error_hidden(self, error_locator):
        self.wait.until_not(EC.visibility_of_element_located(error_locator))

