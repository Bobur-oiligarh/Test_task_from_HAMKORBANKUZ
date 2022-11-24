from unittest import TestCase

from test_reqres.tests.steps.delete_user_steps import step_delete_user
from test_reqres.tests.steps.get_single_user_steps import step_get_single_user
from test_reqres.tests.steps.get_users_steps import step_get_users
from test_reqres.tests.steps.patch_user_steps import step_patch_user
from test_reqres.tests.steps.post_user_steps import step_post_user
from test_reqres.tests.steps.put_user_steps import step_put_user


class ReqresCase(TestCase):

    @classmethod
    def setUp(cls) -> None:
        pass

    @classmethod
    def test_get_users(cls):
        step_get_users()

    @classmethod
    def test_get_single_user(cls):
        step_get_single_user()

    @classmethod
    def test_post_user(cls):
        step_post_user()

    @classmethod
    def test_put_user(cls):
        step_put_user()

    @classmethod
    def test_patch_user(cls):
        step_patch_user()

    @classmethod
    def test_delete_user(cls):
        step_delete_user()


