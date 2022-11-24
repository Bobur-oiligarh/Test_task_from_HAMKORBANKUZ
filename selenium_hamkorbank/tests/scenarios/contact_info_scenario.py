from selenium_hamkorbank.tests.steps.contact_info.contact_info_steps import step_short_short_number, \
    step_2_full_numbers, step_feedback_element, step_check_social_media_icons


def contact_info_block_scenario(context):
    step_short_short_number(context)
    step_2_full_numbers(context)
    step_feedback_element(context)
    step_check_social_media_icons(context)
