from test_reqres.http_requests.get_single_user import GetSingleUser


def step_get_single_user():
    response = GetSingleUser().response()
    response.check_status(200).check_parameters_in_data()
    response.check_params_in_support_data("url")
    response.check_params_in_support_data("text")

