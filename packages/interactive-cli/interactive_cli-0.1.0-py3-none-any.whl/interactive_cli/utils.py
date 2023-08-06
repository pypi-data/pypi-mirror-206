from typing import Any, Iterable


def index(search: Any, iterable: Iterable[Any]) -> int:
    for i, value in enumerate(iterable):
        if search == value:
            return i

    raise ValueError(f"Search {search} was not found")
