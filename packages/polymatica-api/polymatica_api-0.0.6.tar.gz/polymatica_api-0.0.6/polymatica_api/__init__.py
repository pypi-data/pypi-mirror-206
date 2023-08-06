from .types import Dataset, Data
from .data_option import DataOption

import typing
import requests
import urllib.parse


HOST_ROUTE = dict(
    dataset='/proxy/manager/api/v1/dataset',
    data_dataset='/proxy/manager/api/v1/data/dataset',
)


class PolymaticaAPI:
    _host: str
    _session: requests.Session

    def __init__(self, host, token):
        self._host = host
        self._session = requests.session()
        self._session.headers = {
            "Authorization": token
        }

    def from_dataset(self, name) -> DataOption:
        return DataOption(name, self)

    def get_dataset(self, name) -> typing.Optional[Dataset]:
        data = self._session.get(self.route('dataset'), params=dict(
            name=name
        )).json()

        for item in data.get('rows'):
            dataset = Dataset.parse_obj(item)
            if dataset.name == name:
                return dataset
        return None

    def get_data(self, options, get_columns: bool = True, get_dataset: bool = False):
        data = self._session.post(self.route('data_dataset'), json=dict(
            data_options=list(map(lambda item: item.make(), options)),
            get_columns=get_columns,
            get_dataset=get_dataset
        )).json()

        result = dict()
        for key in data:
            result[key] = Data.parse_obj(data[key])

        return result

    def route(self, name: str) -> str:
        if name not in HOST_ROUTE:
            raise Exception(f'Route "{name}" not found')
        return urllib.parse.urljoin(self._host, HOST_ROUTE[name])