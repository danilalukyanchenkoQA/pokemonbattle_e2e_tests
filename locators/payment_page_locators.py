from selenium.webdriver.common.by import By

class PaymentPageLocators:

    CARD_NUMBER = (By.CLASS_NAME, "card_number")
    CARD_ACTUAL = (By.CLASS_NAME, "card_date")
    CSV_INPUT = (By.CLASS_NAME, "card_csv")
    NAME_INPUT = (By.CLASS_NAME, "card_name")

    PAY_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Оплатить')]")

    SMS_CODE_INPUT = (By.CLASS_NAME, "threeds_number")
    SEND_CODE_BUTTON = (By.XPATH, "//button[text()='Оплатить']")
    SUCCESS_TITLE = (By.XPATH, "//h3[contains(text(), 'Покупка прошла успешно')]")

    # ДЛЯ СКРИНШОТНЫХ ТЕСТОВ
    CARD_ERROR = (By.XPATH, "//span[contains(@class, 'style_1_base_input_error') and contains(text(), 'Неверный номер карты')]")
    EXPIRY_ERROR = (By.XPATH, "//span[contains(@class, 'style_1_base_input_error') and contains(text(), 'Неверный срок')]")
    PAYMENT_FORM = (By.TAG_NAME, "form")
