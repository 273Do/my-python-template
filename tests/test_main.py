from main import sum_even_numbers


def test_sum_even_numbers_all_even() -> None:
    assert sum_even_numbers([2, 4, 6, 8]) == 20


def test_sum_even_numbers_mixed() -> None:
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12


def test_sum_even_numbers_all_odd() -> None:
    assert sum_even_numbers([1, 3, 5, 7]) == 0


def test_sum_even_numbers_empty() -> None:
    assert sum_even_numbers([]) == 0
