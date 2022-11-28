import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 6го элемента основного меню сайд бара")
def step_seventh_el_of_main_menu(context):
    text = context.text_data["main_menu"][7]["main"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.ISTEMOLCHI_BURCHAGI_BUTTON, text)
