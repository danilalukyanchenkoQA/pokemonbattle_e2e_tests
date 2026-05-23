Pokémon Battle E2E Tests

🎯 Описание проекта
Автоматизированные E2E тесты для веб-приложения Pokémon Battle (pokemonbattle.ru). 
Тестирование покупки Premium подписки, оплаты картой, 3DS верификации и отмены подписки.

🚀 Основной функционал
✅ Покупка Premium подписки
✅ Оплата тестовой картой (3DS Secure)
✅ SMS верификация
✅ Отмена Premium подписки
✅ Allure отчеты с скриншотами и шагами
✅ Автоматическая очистка Premium перед тестами

📁 Структура проекта
text
pokemonbattle_e2e_tests/
├── tests/e2e/              # Тесты E2E
│   └── test_trainer_page.py
├── data/                   # Тестовые данные
│   ├── payment_data.py     # Карты, SMS коды
│   └── test_trainer_data.py
├── locators/               # Локаторы страниц
│   ├── premium_page_locators.py
│   ├── payment_page_locators.py
│   ├── trainer_page_locators.py
│    ├── login_page_locators.py
│    ├── pokemons_list_locators.py
│
├── conftest.py             # Фикстуры (driver, cleanup)
├── requirements.txt        # Зависимости
└── README.md

🛠 Установка и запуск
1. Клонирование и установка
bash
git clone <repository>
cd pokemonbattle_e2e_tests
pip install -r requirements.txt
2. Настройка токенов
Создай .env файл:
text
POKEMONBATTLE_TOKEN=твой_trainer_token
3. Запуск тестов
bash
# Обычный запуск
pytest tests/e2e/

# 🚀 С Allure отчетами
pytest --alluredir=allure-results
allure serve allure-results
allure generate .\allure-results\ - Для генерации HTML отчета, который удобно передавать кому-либо
allure generate allure-results --single-file -o allure-report/complete.html
4. Быстрый скрипт
bash
./run_tests.bat  # Windows
./run_tests.sh   # Linux/Mac

🐍 Python 3.8+
🔧 Pytest 7.4+
🌐 Selenium WebDriver + Chrome
📊 Allure Framework
🎛 webdriver-manager
📦 python-dotenv
🎯 Локаторы страниц
TrainerPage - навигация, кнопки
PremiumPage - покупка Premium
PaymentPage - форма оплаты, 3DS
PokemonsList - список покемонов

🚀 Готово к запуску! pytest tests/e2e/ --alluredir=allure-results && allure serve allure-results 🔥