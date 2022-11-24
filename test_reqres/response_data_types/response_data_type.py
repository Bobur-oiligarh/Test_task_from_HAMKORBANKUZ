from abc import ABC, abstractmethod
from unittest import TestCase

import allure


class BaseType(ABC):

    def __init__(self):
        self._tc = TestCase()

    @abstractmethod
    def check(self):
        pass

    @allure.step("Проверка значения параметра {param_name} - на наличие и 'string' типа")
    def assert_param_not_empty_str(self, param_name: str):
        value = getattr(self, param_name)
        self._assert_not_none(param_name)
        self._assert_true_type(param_name, str)
        self._tc.assertNotEqual(value, "")

    @allure.step("Проверка значения параметра {param_name} - на None и 'integer' тип")
    def assert_param_not_none_and_int(self, param_name: str):
        self._assert_not_none(param_name)
        self._assert_true_type(param_name, int)

    @allure.step("Проверка значение параметра {param_name} на null")
    def _assert_not_none(self, param_name: str):
        value = getattr(self, param_name)
        self._tc.assertIsNotNone(value)

    @allure.step("Проверка значения параметра {param_name} на тип integer")
    def _assert_true_type(self, param_name: str, expected_type):
        value = getattr(self, param_name)
        self._tc.assertIsInstance(value, expected_type)

    @allure.step("Проверка объектов в листе data")
    def check_all_params_of_users_in_list(self, list_attr_name: str):
        for obj in getattr(self, list_attr_name):
            obj.check()


class BaseTypeParent(BaseType, ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    def deserialize_data_to_list_of_objects(object_type: type, data: list):
        result = []
        for item in data:
            result.append(object_type(item))
        return result


class ReqresUser(BaseType):
    def __init__(self, data: dict):
        super().__init__()
        self.id = data.get("id")
        self.email = data.get("email")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.avatar = data.get("avatar")

    def check(self, **kwargs):
        self.assert_param_not_none_and_int("id")
        self.assert_param_not_empty_str("email")
        self.assert_param_not_empty_str("first_name")
        self.assert_param_not_empty_str("last_name")
        self.assert_param_not_empty_str("avatar")


class Users(BaseTypeParent):
    def __init__(self, data):
        super().__init__()
        self.users = self.deserialize_data_to_list_of_objects(ReqresUser, data)

    def check(self, **kwargs):
        self.check_all_params_of_users_in_list("users")

