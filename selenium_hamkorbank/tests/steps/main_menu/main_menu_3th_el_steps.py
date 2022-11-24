import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 3го элемента основного меню сайд бара")
def step_third_el_of_main_menu(context):
    text = context.text_data["main_menu"][3]["main"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.MAIN_MENU_THIRD, text)


@allure.step("Проверка видимости и правильности текстов у субменю 3го элемента")
def step_submenu_of_third_el(context):
    list_of_expected_text = context.text_data["main_menu"][3]["sub"]
    main_page = MainPage(context.driver)
    main_page.do_hover(SideBarLocators.MAIN_MENU_THIRD)
    main_page.check_text_in_submenu_list(list_of_expected_text, submenu_locator=SideBarLocators.MAIN_MENU_THIRD_SUBMENU)
