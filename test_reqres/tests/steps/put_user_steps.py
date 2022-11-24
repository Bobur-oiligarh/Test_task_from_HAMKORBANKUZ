from test_reqres.http_requests.put_user_param import PutUser


def step_put_user():
    response = PutUser().response()
    response.check_status(200)
    response.check_param_not_none_and_true_type("name", str)
    response.check_param_not_none_and_true_type("job", str)
    response.check_param_not_none_and_true_type("updatedAt", str)
