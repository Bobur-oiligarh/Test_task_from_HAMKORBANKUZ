from unittest import TestCase
from test_reqres.http_requests.delete_user import DeleteUser
from requests.status_codes import codes
import allure


@allure.step("Проверка статус код ответа")
def step_delete_user():
    response = DeleteUser().response()
    status_code = response.status_code
    TestCase().assertEqual(status_code, codes.no_content)

