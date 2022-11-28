import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 1го элемента top menu")
def step_first_el_of_menu_1(context):
    text = context.text_data["top_menu"][0]["first"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.INTERNET_BANKING_BUTTON, text)


@allure.step("Проверка 2го элемента top menu")
def step_second_el_of_menu_1(context):
    text = context.text_data["top_menu"][1]["second"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.FOYDANGIZNI_XISOBLANG_BUTTON, text)
