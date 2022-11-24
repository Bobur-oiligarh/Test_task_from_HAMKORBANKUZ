from utils.api_utils.http_client import BaseRequest
from test_reqres.response_data_types.response_data_type import ReqresUser


class GetSingleUser(BaseRequest):
    def __init__(self):
        super().__init__(
            endpoint="/api/users/2",
            method="get",
            data_type=ReqresUser
        )
