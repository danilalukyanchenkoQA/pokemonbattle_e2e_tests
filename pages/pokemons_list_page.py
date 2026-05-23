from pages.base_page import BasePage
from locators.pokemons_list_locators import PokemonsListLocators
from data.test_trainer_data import TRAINER_ID


class PokemonsListPage(BasePage):
    TRAINER_URL = f"https://pokemonbattle.ru/trainer/{TRAINER_ID}"

    def go_to_trainer_page(self):
        """Переход на страницу тренера"""
        self.click(PokemonsListLocators.trainer_card)
        assert self.driver.current_url == self.TRAINER_URL
        from pages.trainer_page import TrainerPage
        return TrainerPage(self.driver)

