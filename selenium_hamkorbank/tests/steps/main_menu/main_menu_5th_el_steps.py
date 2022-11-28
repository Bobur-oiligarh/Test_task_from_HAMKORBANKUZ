import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 5го элемента основного меню сайд бара")
def step_fifth_el_of_main_menu(context):
    text = context.text_data["main_menu"][5]["main"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.BANK_TOGRISIDA_BUTTON, text)


@allure.step("Проверка видимости и правильности текстов у субменю 5го элемента")
def step_submenu_of_fifth_el(context):
    list_of_expected_text = context.text_data["main_menu"][5]["sub"]
    main_page = MainPage(context.driver)
    main_page.do_hover(SideBarLocators.BANK_TOGRISIDA_BUTTON)
    main_page.check_text_in_submenu_list(list_of_expected_text, SideBarLocators.SUBMENU_BANK_TOGRISIDA)
