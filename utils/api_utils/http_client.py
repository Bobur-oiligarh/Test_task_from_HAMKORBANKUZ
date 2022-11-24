from typing import Any
from urllib.parse import urljoin

import requests

from utils.api_utils.http_response import HttpResponse

methods = {
    "post": requests.post,
    "get": requests.get,
    "put": requests.put,
    "delete": requests.delete,
    "patch": requests.patch
}


class BaseRequest:
    BASE_URL = "https://reqres.in/"

    def __init__(self, endpoint: str, method: str, data_type: Any = None, params: dict = None, data: dict = None):
        self._base_url = self.BASE_URL
        self._endpoint = endpoint
        self._method = method
        self._data_type = data_type
        self._params = params
        self._data = data
        self._response = None

    def _make_request(self):
        response = methods[self._method](
            url=self._url,
            params=self._params,
            data=self._data
        )
        if self._method == "delete":
            return response
        self._response = HttpResponse(response, self._data_type)
        return self._response

    def response(self):
        return self._make_request()

    @property
    def _url(self):
        return urljoin(self._base_url, self._endpoint)

