import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 2го элемента основного меню сайд бара")
def step_second_el_of_main_menu(context):
    text = context.text_data["main_menu"][2]["main"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.MAIN_MENU_SECOND, text)


@allure.step("Проверка видимости и правильности текстов у субменю 2го элемента")
def step_submenu_of_second_el(context):
    list_of_expected_text = context.text_data["main_menu"][2]["sub"]
    main_page = MainPage(context.driver)
    main_page.do_hover(SideBarLocators.MAIN_MENU_SECOND)
    main_page.check_text_in_submenu_list(list_of_expected_text, SideBarLocators.MAIN_MENU_SECOND_SUBMENU)

