from polymatica_api import PolymaticaAPI
from types import DataOptionMethod


p = PolymaticaAPI('https://dev.platform.polymatica.ru', 'Token c1cffe48-b6d5-5575-a38a-2ee75b11af0e')
print(p.get_data([
    p.from_dataset('Медицина.xlsx').
    method(DataOptionMethod.Aggregate).
    group("Пол").
    sum('Количество вызовов врача', 'Количество звонков в больницу').
    avg('Количество посещений больницы')
], True, False))
