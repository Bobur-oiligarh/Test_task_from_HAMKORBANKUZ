import allure

from selenium_hamkorbank.tests.steps.top_menu.top_menu_steps import step_first_el_of_menu_1, step_second_el_of_menu_1


@allure.step("Проверка топ меню сайд бара")
def sidebar_top_menu_scenario(context):
    step_first_el_of_menu_1(context)
    step_second_el_of_menu_1(context)
