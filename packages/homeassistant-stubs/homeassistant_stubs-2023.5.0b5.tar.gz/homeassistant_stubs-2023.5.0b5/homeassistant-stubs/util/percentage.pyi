from typing import TypeVar

_T = TypeVar('_T')

def ordered_list_item_to_percentage(ordered_list: list[_T], item: _T) -> int: ...
def percentage_to_ordered_list_item(ordered_list: list[_T], percentage: int) -> _T: ...
def ranged_value_to_percentage(low_high_range: tuple[float, float], value: float) -> int: ...
def percentage_to_ranged_value(low_high_range: tuple[float, float], percentage: int) -> float: ...
def states_in_range(low_high_range: tuple[float, float]) -> float: ...
def int_states_in_range(low_high_range: tuple[float, float]) -> int: ...
