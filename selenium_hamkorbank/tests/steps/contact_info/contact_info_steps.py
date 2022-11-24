import allure

from selenium_hamkorbank.pages.locators import SideBarLocators
from selenium_hamkorbank.pages.page import MainPage


@allure.step("Проверка короткого номера доверия на контакт блоке на визуальность, кликабельность, и текста")
def step_short_short_number(context):
    expected_text = "1256"
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.SHORT_NUMBER, expected_text)


@allure.step("Проверка 2х полных номеров связи указанных на контакт инфо блоке")
def step_2_full_numbers(context):
    main_page = MainPage(context.driver)
    list_of_full_phone_numbers_from_page = (main_page.find_elements(SideBarLocators.FULL_NUMBERS_ELEMS))[1:]
    expected_numbers_list = context.text_data.get("contact_info").get("full_numbers")
    for index, elem in enumerate(list_of_full_phone_numbers_from_page):
        main_page.element_if_visible(elem)
        main_page.element_to_be_clickable(elem)
        main_page.text_to_be_present_in_element(expected_numbers_list[index], elem)


@allure.step("Проверка блока с параллелограмной рамкой и текстом 'ОБРАТНАЯ СВЯЗЬ'")
def step_feedback_element(context):
    feedback_field_text = context.text_data.get("contact_info").get("feedback_text")
    main_page = MainPage(context.driver)
    main_page.check_elem_visible_clickable_true_text(SideBarLocators.FEEDBACK_ELEMENT, feedback_field_text)


@allure.step("Проверка 4 иконок социальных сетей")
def step_check_social_media_icons(context):
    main_page = MainPage(context.driver)
    list_icons = main_page.find_elements(SideBarLocators.SOCIAL_MEDIA_ICONS_LI_EL)

    for index, icon_elem in enumerate(list_icons):
        with allure.step(f" Проверка {index + 1}й иконки на визуабельность, кликабельность"):
            pass
        main_page.element_if_visible(icon_elem)
        main_page.element_to_be_clickable(icon_elem)
