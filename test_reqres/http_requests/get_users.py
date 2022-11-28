from utils.api_utils.http_client import BaseRequest
from test_reqres.response_data_types.response_data_type import Users


class GetUsers(BaseRequest):
    def __init__(self):
        super().__init__(
            endpoint="/api/users",
            method="get",
            data_type=Users,
            params={"page": 2}
        )
