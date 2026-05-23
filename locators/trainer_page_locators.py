from selenium.webdriver.common.by import By

class TrainerPageLocators:
    premium_button = (By.XPATH, "//div[contains(@class, 'k_trainer_in_button_title') and text()='Pokemon Premium']")
    MOSCOW_LOCATION = (
        By.XPATH,
        "//div[normalize-space(text())='Moscow']"
    )
    TRAINER_CARD = (
        By.CLASS_NAME, "single_page_body_content_inner_box")

    ACHIEVEMENTS = (
        By.CSS_SELECTOR, ".achievements"
    )

    LEVEL_NUMBER = (
        By.XPATH,
        "//span[contains(@class, 'single_page_body_content_inner_top_list_attr_one_text') and normalize-space(text())='3']")

    POKEBALLS = (
        By.XPATH,
        "//span[contains(@class, 'single_page_body_content_inner_top_list_attr_one_text') and normalize-space(text())='0']")