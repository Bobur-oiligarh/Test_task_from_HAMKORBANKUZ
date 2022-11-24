from test_reqres.http_requests.get_users import GetUsers


def step_get_users():
    response = GetUsers().response()
    response.check_status(200)
    response.check_param_not_none_and_true_type("page", int)
    response.check_param_not_none_and_true_type("per_page", int)
    response.check_param_not_none_and_true_type("total", int)
    response.check_param_not_none_and_true_type("total_pages", int)
    response.check_parameters_in_data()
    response.check_params_in_support_data("url").check_params_in_support_data("text")
