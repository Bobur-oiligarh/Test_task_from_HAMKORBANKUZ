from selenium_hamkorbank.tests.steps.main_menu.main_menu_1th_el_steps import step_first_el_of_main_menu, \
    step_submenu_of_first_el
from selenium_hamkorbank.tests.steps.main_menu.main_menu_2th_el_steps import step_second_el_of_main_menu, \
    step_submenu_of_second_el
from selenium_hamkorbank.tests.steps.main_menu.main_menu_3th_el_steps import step_third_el_of_main_menu, \
    step_submenu_of_third_el
from selenium_hamkorbank.tests.steps.main_menu.main_menu_4th_el_steps import step_fourth_el_of_main_menu, \
    step_submenu_of_fourth_el
from selenium_hamkorbank.tests.steps.main_menu.main_menu_5th_el_steps import step_fifth_el_of_main_menu, \
    step_submenu_of_fifth_el
from selenium_hamkorbank.tests.steps.main_menu.main_menu_6th_el_steps import step_sixth_el_of_main_menu
from selenium_hamkorbank.tests.steps.main_menu.main_menu_7th_el_steps import step_seventh_el_of_main_menu


def main_menu_of_sidebar(context):
    step_first_el_of_main_menu(context)
    step_submenu_of_first_el(context)

    step_second_el_of_main_menu(context)
    step_submenu_of_second_el(context)

    step_third_el_of_main_menu(context)
    step_submenu_of_third_el(context)

    step_fourth_el_of_main_menu(context)
    step_submenu_of_fourth_el(context)

    step_fifth_el_of_main_menu(context)
    step_submenu_of_fifth_el(context)

    step_sixth_el_of_main_menu(context)

    step_seventh_el_of_main_menu(context)
