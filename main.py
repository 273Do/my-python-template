import os
import sys
from pathlib import Path


def sum_even_numbers(numbers: list[int]) -> int:
    """Given a list of integers, return the sum of all even numbers in the list."""
    result = sum(num for num in numbers if num % 2 == 0)
    print(result)
    return result


def show_exec_info() -> None:
    print(Path(__file__).resolve())
    print(os.path.abspath(__file__))  # noqa: PTH100
    print(sys.path)


sum_even_numbers([1, 2, 3, 4, 5, 6])
print("--")
show_exec_info()
