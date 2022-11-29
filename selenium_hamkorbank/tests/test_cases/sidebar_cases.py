import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from parameterized import parameterized
from selenium_hamkorbank.test_data.context import Context
from selenium_hamkorbank.test_data.yaml_reader import HamkorbankuzText
from selenium_hamkorbank.tests.scenarios.contact_info_scenario import sidebar_contact_info_block_scenario
from selenium_hamkorbank.tests.scenarios.main_menu_scenario import sidebar_main_menu_scenario
from selenium_hamkorbank.tests.scenarios.top_menu_scenario import sidebar_top_menu_scenario


class HamkorSideBar(unittest.TestCase):

    def setUp(self):

        self._url = "https://www.hamkorbank.uz/"
        self._text_data = HamkorbankuzText().uz
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(100)
        self.driver.maximize_window()
        self.driver.get(self._url)

        self.context = Context(driver=self.driver, url=self._url, text_data=self._text_data)

    @staticmethod
    def change_language_to_ru(driver):
        lang_button = driver.find_element(By.LINK_TEXT, "UZ")
        ActionChains(driver).move_to_element(lang_button).perform()
        ru_lang = driver.find_element(By.LINK_TEXT, "RU")
        ActionChains(driver).move_to_element(ru_lang).click().perform()

    @parameterized.expand([("uz"), ("ru")])
    def test_sidebar(self, language):
        if language == "ru":
            self.change_language_to_ru(self.driver)
            self._text_data = HamkorbankuzText().ru
            self.context = Context(driver=self.driver, url=self._url, text_data=self._text_data)

        # checking side bar in uzbek lang
        sidebar_top_menu_scenario(self.context)
        sidebar_main_menu_scenario(self.context)
        sidebar_contact_info_block_scenario(self.context)

    def tearDown(self):
        self.context.driver.close()



