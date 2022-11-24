from test_reqres.http_requests.post_user import PostUser


def step_post_user():
    response = PostUser().response()
    response.check_status(201).check_param_not_none_and_true_type("name", str)
    response.check_param_not_none_and_true_type("job", str)
    response.check_param_not_none_and_true_type("id", str)
    response.check_param_not_none_and_true_type("createdAt", str)

