import re
from typing import Iterator, List, Iterable, Set, Union


class Search:

    def filter_(self: Iterator, string_to_search: str) -> Iterable:
        """Get data which contain specified text"""
        if not isinstance(string_to_search, str):
            raise TypeError("Wrong data passed to the filter function, only strings allowed")
        return filter(lambda line: string_to_search in line, self)

    def sort_(self: Iterator, order: str = 'asc') -> List:
        """Sort data in ascending or descending order"""
        if order not in ('asc', 'desc'):
            raise ValueError('Wrong argument passed to the sort function, only asc or desc are allowed')
        if order == 'desc':
            return sorted(self, reverse=True)
        return sorted(self, reverse=False)

    def map_(self: Iterator, column: Union[str, int]) -> Iterable:
        """Get only column specified"""

        regex = re.compile(r'(?: - - \[)|(?:\] ")|(?:" ")|(?: \")|(?:\" )')

        if not str(column).isdigit():
            raise TypeError('Negative number or text passed as a column number to the map function')

        return map(lambda line: regex.split(line)[int(column)], self)

    def limit_(self: Iterator, number: Union[str, int]) -> List:
        """Limit lines returned by the number passed"""
        if not str(number).isdigit():
            raise TypeError('Not digit passed to the limit function, only digits allowed')
        return list(self)[:int(number)]

    def unique_(self: Iterator, *args) -> Set:
        """Return only unique lines"""
        return set(self)

    def regex_(self: Iterator, expression: str) -> Iterable:
        """Filter data with regular expression passed"""
        regex = re.compile(rf'{str(expression)}')
        return filter(lambda line: regex.search(line), self)
