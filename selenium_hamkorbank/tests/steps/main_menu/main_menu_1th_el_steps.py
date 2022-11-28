import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка 1го элемента основного меню сайд бара")
def step_first_el_of_main_menu(context):
    text = context.text_data["main_menu"][1]["main"]
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.JISMONIY_SHAXSLARGA_BUTTON, text)


@allure.step("Проверка видимости и правильности текстов у субменю 1го элемента")
def step_submenu_of_first_el(context):
    list_of_expected_text = context.text_data["main_menu"][1]["sub"]
    main_page = MainPage(context.driver)
    main_page.do_hover(SideBarLocators.JISMONIY_SHAXSLARGA_BUTTON)
    main_page.check_text_in_submenu_list(list_of_expected_text, submenu_locator=SideBarLocators.SUBMENU_JISMONIY_SHAXSLARGA)
