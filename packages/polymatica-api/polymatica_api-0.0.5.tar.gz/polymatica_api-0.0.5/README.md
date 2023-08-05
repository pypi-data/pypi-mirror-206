This is a simple example of getting data from a server Polymatica Platform

```python
from polymatica_api import PolymaticaAPI
from polymatica_api.types import DataOptionMethod


p = PolymaticaAPI('{SERVER_URL}', 'Token {TOKEN}')
print(p.get_data([
    p.from_dataset('world_population.csv').
    method(DataOptionMethod.Aggregate).
    group("Country/Territory").
    sum(
        '2000 Population', 
        '2010 Population', 
        '2015 Population',
        '2020 Population',
        '2022 Population',
    )
], False, False))
```