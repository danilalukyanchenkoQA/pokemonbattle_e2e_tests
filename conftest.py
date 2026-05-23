import json
from urllib.parse import urlparse, parse_qs

import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page_locators import LoginPageLocators
import os
from selenium.webdriver.common.by import By

from locators.pokemons_list_locators import PokemonsListLocators
from locators.trainer_page_locators import TrainerPageLocators

import logging
import time
from requests.exceptions import RequestException

from pages.pokemons_list_page import PokemonsListPage

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def load_environment():
    load_dotenv()


@pytest.fixture(scope='function')
def user_login(driver):
    driver.get("https://pokemonbattle.ru")
    login_input = driver.find_element(*LoginPageLocators.login_input)
    login_input.send_keys(os.getenv("LOGIN"))
    password_input = driver.find_element(*LoginPageLocators.password_input)
    password_input.send_keys(os.getenv("PASSWORD"))
    login_button = driver.find_element(*LoginPageLocators.login_button)
    login_button.click()
    # ПРОВЕРКА: главная загружена
    WebDriverWait(driver, 10).until(lambda d: "login" not in d.current_url)
    assert driver.current_url == "https://pokemonbattle.ru/"  # ← ФИКСТУРА!
    yield driver


@pytest.fixture(scope='function')
def trainer_page(driver, user_login):
    driver.find_element(*PokemonsListLocators.trainer_card).click()
    #  ПРОВЕРКА: страница тренера загружена
    WebDriverWait(driver, 10).until(lambda d: "/trainer/" in d.current_url)
    assert "/trainer/" in driver.current_url  # ← ФИКСТУРА
    yield driver


@pytest.fixture(scope='function')
def premium_page(driver, user_login):
    driver.find_element(*PokemonsListLocators.trainer_card).click()
    #  ПРОВЕРКА: страница тренера загружена!
    WebDriverWait(driver, 10).until(lambda d: "/trainer/" in d.current_url)
    assert "/trainer/" in driver.current_url  # ← ФИКСТУРА!
    driver.find_element(*TrainerPageLocators.premium_button).click()
    #  ПРОВЕРКА: страница покупки Premium загружена
    WebDriverWait(driver, 10).until(lambda d: "/premium" in d.current_url)
    assert driver.current_url == "https://pokemonbattle.ru/premium"  # ← ФИКСТУРА
    yield driver


@pytest.fixture(scope="session")
def api_session():
    """Requests Session с токеном"""
    session = requests.Session()
    session.headers.update({"trainer_token": os.getenv("POKEMONBATTLE_TOKEN")})
    yield session
    session.close()


@pytest.fixture(scope="function")
def premium_cleanup(api_session):
    """Очистка ТОЛЬКО для тестов, которые её просят"""
    try:
        response = api_session.post("https://lavka.pokemonbattle.ru/cancel_premium")
        print(f"🧹 Cleanup статус: {response.status_code}")
    except:
        pass
    yield

@pytest.fixture
def pokemons_list_page(driver, user_login):
    """Главная страница с покемонами"""
    driver.get("https://pokemonbattle.ru/")
    return PokemonsListPage(driver)


@pytest.fixture
def navigate_to_payment(driver, user_login):
    """Навигация до payment_page (из test_buy_premium)"""
    pokemons_page = PokemonsListPage(driver)
    trainer_page = pokemons_page.go_to_trainer_page()
    premium_page = trainer_page.go_to_premium()
    premium_page.set_days()

    payment_page = premium_page.buy_premium()  # Возвращаем payment_page!
    return payment_page
