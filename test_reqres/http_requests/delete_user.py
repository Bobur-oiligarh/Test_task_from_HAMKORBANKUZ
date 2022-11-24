from utils.api_utils.http_client import BaseRequest


class DeleteUser(BaseRequest):
    def __init__(self):
        super().__init__(
            endpoint="/api/users/2",
            method="delete",
            data_type=None
        )

