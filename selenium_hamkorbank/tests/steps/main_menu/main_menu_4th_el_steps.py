import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 4го элемента основного меню сайд бара")
def step_fourth_el_of_main_menu(context):
    text = context.text_data["main_menu"][4]["main"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.MAIN_MENU_FOURTH, text)


@allure.step("Проверка видимости и правильности текстов у субменю 4го элемента")
def step_submenu_of_fourth_el(context):
    list_of_expected_text = context.text_data["main_menu"][4]["sub"]
    main_page = MainPage(context.driver)
    main_page.do_hover(SideBarLocators.MAIN_MENU_FOURTH)
    main_page.check_text_in_submenu_list(list_of_expected_text, SideBarLocators.MAIN_MENU_FOURTH_SUBMENU)
