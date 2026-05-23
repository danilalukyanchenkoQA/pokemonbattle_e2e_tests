from selenium.webdriver.common.by import By

class PremiumPageLocators:
    BEGINNING_ACHIEVEMENT_ACTIVE = (
        By.CSS_SELECTOR,
        "div.achievements_icon.beginning-icon.active[data-slug='beginning']"
    )

    PREMIUM_DAYS = (
        By.CSS_SELECTOR,
        ".auth__wrap.k_input_premium input[name='day']"
    )

    BUY_PREMIUM_BUTTON = (By.ID, "buy-premium")

    CANCEL_PREMIUM_BUTTON = (By.ID, "cancel-premium")
    SUBMIT_CANCEL_PREMIUM_BUTTON = (By.ID, "cancel-go-premium")
    SUCCESS_TITLE = (By.XPATH,"//div[contains(text(), 'Вы отменили подписку :(')]")

    DAYS_INPUT = (By.CSS_SELECTOR, "input[name='days'], [data-test='days-input']")
    COST_DAYS = (
        By.CSS_SELECTOR,
        ".k_skidka_premium"
    )
