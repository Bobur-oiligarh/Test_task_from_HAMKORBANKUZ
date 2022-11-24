import pathlib
from pprint import pprint

import yaml


class HamkorbankuzText:
    _FILE_ABS_PATH = pathlib.Path(__file__).parent.joinpath("sidebar_text.yaml")

    def __init__(self):
        self.uz: dict = self._read()["uz"]
        self.ru: dict = self._read()['ru']

    def _read(self):
        with open(self._FILE_ABS_PATH, "r") as f:
            read_data = yaml.load(f, Loader=yaml.FullLoader)
        return read_data


if __name__ == '__main__':
    d = HamkorbankuzText()._read()
    pprint(d)
