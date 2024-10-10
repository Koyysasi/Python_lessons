from typing import List, Dict, Tuple, Union, Any, Optional, Callable


def typehint(x: int) -> int:
	return x


def add_first_two(l: List[Union[int, float]]) -> Union[int, float]:
	return l[0] + l[1]


if __name__ == "__main__":
	print(add_first_two([1,0,4,2,4,6,6]))
