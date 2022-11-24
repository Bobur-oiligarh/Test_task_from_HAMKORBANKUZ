from utils.api_utils.http_client import BaseRequest


class PatchUser(BaseRequest):
    def __init__(self):
        super().__init__(
            endpoint="/api/users/2",
            method="patch",
            data_type=None,
            data={"name": "morpheus", "job": "zion resident"}
        )
