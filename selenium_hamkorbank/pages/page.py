from unittest import TestCase
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_hamkorbank.pages.element import BasePageElement
from selenium.common.exceptions import StaleElementReferenceException

from selenium_hamkorbank.pages.locators import SideBarLocators


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self._tc = TestCase()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def do_hover(self, locator: tuple):
        element_to_hover_over = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Визуабельность, кликабельность, правильность текста элемента")
    def check_elem_visible_clickable_true_text(self, locator: tuple, expected_text: str):
        element = self.driver.find_element(*locator)
        self.element_if_visible(element)
        self.element_to_be_clickable(element)
        self.text_to_be_present_in_element(expected_text, element)

    @allure.step("Проверка визуабельности")
    def element_if_visible(self, element):
        self._tc.assertTrue(element.is_displayed(), msg="Элемент не видим на странице")

    @allure.step("Проверка кликабельности")
    def element_to_be_clickable(self, element):
        self._tc.assertTrue(element.is_enabled(), msg=f"Элемент не кликабельный")

    @allure.step("Проверка текста элемента")
    def text_to_be_present_in_element(self, expected_text: str, element):
        element_text = element.text
        self._tc.assertEqual(expected_text, element_text,
                             msg=f"Текст элемента: '{element_text}' не совпадает с ожидаемым '{expected_text}'")

    @allure.step("Проверка текста элементов субменю")
    def check_text_in_submenu_list(self, list_of_expected_text: list, submenu_locator: tuple):
        WebDriverWait(self.driver, 20).until(EC.visibility_of(self.driver.find_element(*submenu_locator)))
        submenu_elem_list = self.driver.find_elements(*submenu_locator)

        length_of_actual_list = len(submenu_elem_list)
        length_of_expected_list = len(list_of_expected_text)
        self._tc.assertEqual(length_of_expected_list, length_of_actual_list, msg="Не все элементы в субменю отражается правильно")

        for i in range(length_of_expected_list):
            self._tc.assertEqual(list_of_expected_text[i], submenu_elem_list[i].text,
                                 msg=f" {list_of_expected_text[i]} Не одинаков {submenu_elem_list[i].text}")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.hamkorbank.uz/")
    t = MainPage(driver)

    subloc = SideBarLocators.MAIN_MENU_FIRST_SUBMENU

    t.check_text_in_submenu_list(
        ['Kreditlar', 'Avtokredit', 'Ipoteka kreditlari', 'Omonatlar', 'Plastik kartalar', "Pul o'tkazmalari",
         'Depozit yacheykalari', "O'lchamli oltin quymalar va esdalik tangalar", 'Mobayl banking', 'ЮMoney',
         'Valyuta ayirboshlash shaxobchalari', 'Tariflar'], subloc)
