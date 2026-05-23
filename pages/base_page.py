from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    BASE_URL = "https://pokemonbattle.ru"

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, by_locator: tuple[str, str]):
        """by_locator - это tuple из (by_locator)"""
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def click(self, by_locator: tuple[str, str]):
        elem = self.find(by_locator)
        elem.click()
        return elem

    def type(self, by_locator: tuple[str, str], text:str):
        elem = self.find(by_locator)
        elem.clear()
        elem.send_keys(text)
        return elem

    def element_visible(self, by_locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(by_locator))
