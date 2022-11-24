from typing import Any


class Context:
    def __init__(self, text_data: dict, driver: Any, url: str):
        self.text_data = text_data
        self.driver = driver
        self.page = self.driver.get(url)
