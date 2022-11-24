import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium_hamkorbank.test_data.context import Context
from selenium_hamkorbank.test_data.yaml_reader import HamkorbankuzText
from selenium_hamkorbank.tests.scenarios.contact_info_scenario import contact_info_block_scenario
from selenium_hamkorbank.tests.scenarios.main_menu_scenario import main_menu_of_sidebar
from selenium_hamkorbank.tests.scenarios.top_menu_scenario import top_menu_of_sidebar_scenario


class HamkorSideBar(unittest.TestCase):

    def setUp(self):
        RU = True

        self._url = "https://www.hamkorbank.uz/"
        self._text_data = HamkorbankuzText().uz
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(100)
        self.driver.get(self._url)

        if RU:
            self.change_language_to_ru(self.driver)
            self._text_data = HamkorbankuzText().ru
        self.context = Context(driver=self.driver, url=self._url, text_data=self._text_data)

    @staticmethod
    def change_language_to_ru(driver):
        lang_button = driver.find_element(By.LINK_TEXT, "UZ")
        ActionChains(driver).move_to_element(lang_button).perform()
        ru_lang = driver.find_element(By.LINK_TEXT, "RU")
        ActionChains(driver).move_to_element(ru_lang).click().perform()

    def test_main_menu(self):
        top_menu_of_sidebar_scenario(self.context)
        main_menu_of_sidebar(self.context)
        contact_info_block_scenario(self.context)

    def tearDown(self):
        self.context.driver.close()



