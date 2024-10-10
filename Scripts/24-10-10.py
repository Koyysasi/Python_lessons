from typing import List, Dict, Tuple, Union, Any, Optional, Callable, TypeVar, TypeAlias


def typehint(x: int) -> int:
	return x


def add_first_two(l: List[Union[int, float]]) -> int|float:
	return l[0] + l[1]

T = TypeVar("T")
Point: TypeAlias = tuple[int, int]

def id(x: T) -> T:
	return x


def is_origin(point: Point) -> bool:
	return point[0] == 0 and point[1] == 0


if __name__ == "__main__":
	print(add_first_two([1, 0, 4, 2, 4, 6, 6]))

