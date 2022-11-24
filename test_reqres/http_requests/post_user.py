from utils.api_utils.http_client import BaseRequest


class PostUser(BaseRequest):
    def __init__(self):
        super().__init__(
            endpoint="/api/users",
            method="post",
            data_type=None,
            data={"name": "morpheus", "job": "leader"}
        )
