from unittest import TestCase

import allure
from requests import Response


class HttpResponse:
    def __init__(self, response: Response, data_type: type):
        self._tc = TestCase()
        self._response_text = response.json()
        self.data: data_type = None
        self._status = response.status_code
        self._dict_to_data_type(self._response_text.get("data"), data_type)

    def _dict_to_data_type(self, data, data_type):
        if data and data_type is not None:
            self.data = data_type(data)
        else:
            self.data = data

    @allure.step("Проверка значения ключа 'data'")
    def check_parameters_in_data(self):
        self.data.check()
        return self

    @allure.step("Проверка статус код ответа")
    def check_status(self, expected_status: int):
        self._tc.assertEqual(self._status, expected_status)
        return self

    @allure.step("Проверка значения параметра - {param_name} на наличие и нужного типа")
    def check_param_not_none_and_true_type(self, param_name: str, expected_type: type):
        self._check_param_not_none(param_name)
        self._check_param_is_true_type(param_name, expected_type)

    @allure.step("Проверка значения параметра - {param_name} на наличие")
    def _check_param_not_none(self, param_name):
        self._tc.assertIsNotNone(obj=param_name)

    @allure.step("Проверка значения параметра - {param_name} на правильность типа")
    def _check_param_is_true_type(self, param_name, expected_type):
        value = self._response_text.get(param_name)
        self._tc.assertIsInstance(value, expected_type)

    @allure.step("Проверка значения параметра {param_name} в словаре:'support' на None и string тип")
    def check_params_in_support_data(self, param_name: str):
        value = self._response_text.get("support").get(param_name)
        self._tc.assertIsNotNone(value)
        with allure.step(f"Значение параметра {param_name} не None"):
            pass
        self._tc.assertIsInstance(value, str)
        with allure.step(f"Тип значения параметра {param_name} string"):
            pass
        return self
