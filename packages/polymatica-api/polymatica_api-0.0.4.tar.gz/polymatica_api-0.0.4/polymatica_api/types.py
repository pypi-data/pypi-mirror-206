import datetime
from pydantic import BaseModel
from enum import Enum


class Column(BaseModel):
    id: int
    name: str
    field_type: str
    base_type: int
    path: str
    source_path: str
    update_date: datetime.datetime
    create_date: datetime.datetime


class Dataset(BaseModel):
    id: int
    name: str
    comment: str
    type: str
    columns: list[Column]


class DataOptionBlockAggFn(Enum):
    Any = '-'
    Group = 'group'
    Sum = 'SUM'
    Min = 'MIN'
    Max = 'MAX'
    Average = 'AVG'
    First = 'LAST'
    Last = 'LAST'
    Count = 'COUNT'
    Distinct = 'DISTINCT'
    CountDistinct = 'COUNT_DISTINCT'

    def __str__(self):
        return self.value


class DataOptionMethod(Enum):
    Aggregate = 'aggregate'
    Table = 'table'
    Pivot = 'pivot'

    def __str__(self):
        return self.value



