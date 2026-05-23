from selenium.webdriver.common.by import By

class LoginPageLocators:
    login_input = (By.ID, "k_email")
    password_input = (By.ID, "k_password")
    login_button = (By.CSS_SELECTOR, ".k_form_send_auth")