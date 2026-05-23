from selenium.webdriver.common.by import By
from data.test_trainer_data import TRAINER_ID

class PokemonsListLocators:
    trainer_card_id = (By.XPATH, f"//div[@class='header_card_trainer_id_num' and text()='{TRAINER_ID}']")

    trainer_card = (
        By.XPATH, f"//a[.//div[@class='header_card_trainer_id_num' and text()='{TRAINER_ID}']]"
    )

