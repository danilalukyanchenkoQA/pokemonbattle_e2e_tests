from pages.base_page import BasePage
from locators.premium_page_locators import PremiumPageLocators
from data.payment_data import DAYS


class PremiumPage(BasePage):
    PAYMENT_URL_PATTERN = "/payment"

    def wait_discount_visible(self):
        """Дожидаемся полной видимости стоимости за день"""
        self.wait.until(
            lambda d: d.find_element(*PremiumPageLocators.COST_DAYS).get_attribute("style").strip() == ""
        )

    def set_days(self, days=DAYS):
        """Устанавливает количество дней Premium"""
        days_input = self.find(PremiumPageLocators.PREMIUM_DAYS)
        self.driver.execute_script("arguments[0].value = arguments[1];", days_input, days)
        assert days_input.get_attribute("value") == str(
            days), f"Дней установлено неверно: {days_input.get_attribute('value')}"
        self.wait_discount_visible() #  ожидание анимации

    def buy_premium(self):
        """Кликает Купить → переход на оплату"""
        self.click(PremiumPageLocators.BUY_PREMIUM_BUTTON)
        self.wait.until(lambda d: self.PAYMENT_URL_PATTERN in d.current_url)
        assert self.PAYMENT_URL_PATTERN in self.driver.current_url
        from pages.payment_page import PaymentPage
        return PaymentPage(self.driver)

    def cancel_premium(self):
        """Отменяет Premium подписку"""
        self.click(PremiumPageLocators.CANCEL_PREMIUM_BUTTON)  # Кликаем "Отменить Premium"
        self.click(PremiumPageLocators.SUBMIT_CANCEL_PREMIUM_BUTTON)  # Подтверждаем отмену
        success_title = self.find(PremiumPageLocators.SUCCESS_TITLE)  # Проверяем успешную отмену
        return True