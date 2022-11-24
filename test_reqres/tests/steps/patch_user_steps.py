from test_reqres.http_requests.patch_user_param import PatchUser


def step_patch_user():
    response = PatchUser().response()
    response.check_status(200)
    response.check_param_not_none_and_true_type("name", str)
    response.check_param_not_none_and_true_type("job", str)
    response.check_param_not_none_and_true_type("updatedAt", str)
