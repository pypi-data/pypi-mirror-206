from .types import DataOptionBlockAggFn, DataOptionMethod
from pydantic import BaseModel
from typing import List


class _DataOptionBlock(BaseModel):
    block_name: str
    column_name: str
    agg_fn: DataOptionBlockAggFn


class DataOption:
    def __init__(self, name: str, api):
        self._api = api
        self._name = name

        self._key = "default"
        self._name = ""
        self._method: DataOptionMethod = DataOptionMethod.Table
        self._sort = []
        self._filters = []
        self._offset = 0
        self._limit = 1000
        self._blocks: List[_DataOptionBlock] = []

    def offset(self, value: int):
        self._offset = value
        return self

    def limit(self, value: int):
        self._limit = value
        return self

    def key(self, name: str):
        self._key = name
        return self

    def method(self, name: DataOptionMethod):
        self._method = name
        return self

    def select(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Any)
        return self

    def group(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Group)
        return self

    def sum(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Sum)
        return self

    def min(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Min)
        return self

    def max(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Max)
        return self

    def avg(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Average)
        return self

    def first(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.First)
        return self

    def last(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Last)
        return self

    def count(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Count)
        return self

    def distinct(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.Distinct)
        return self

    def count_distinct(self, *name: str):
        self.add_columns('default', name, DataOptionBlockAggFn.CountDistinct)
        return self

    def add_columns(self, block_name: str, names: List[str], agg_fn: DataOptionBlockAggFn):
        for item in names:
            self._blocks.append(
                _DataOptionBlock(
                    block_name=block_name,
                    column_name=item,
                    agg_fn=agg_fn,
                )
            )
        return self

    def make(self) -> dict:
        dataset = self._api.get_dataset(self._name)

        if not dataset:
            raise Exception(f'Dataset "{self._name}" not found')

        columns_by_name = dict()
        for item in dataset.columns:
            columns_by_name[item.name] = item

        blocks_by_key = dict()
        for item in self._blocks:
            if item.block_name not in blocks_by_key:
                blocks_by_key[item.block_name] = dict(
                    key=item.block_name,
                    columns=[]
                )

            block_columns = blocks_by_key[item.block_name].get('columns')

            column = columns_by_name.get(item.column_name)
            if not column:
                raise Exception(f'Column "{item.column_name}" not found')

            block_columns.append(dict(
                agg_fn=str(item.agg_fn),
                column_id=column.id
            ))

        return dict(
            key=self._key,
            method=str(self._method),
            sort=self._sort,
            filters=self._filters,
            blocks=list(blocks_by_key.values()),
            dataset_id=dataset.id,
            offset=self._offset,
            limit=self._limit,
        )
