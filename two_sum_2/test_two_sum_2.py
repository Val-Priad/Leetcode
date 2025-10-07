import pytest
from two_sum_2.two_sum_2 import twoSum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6]),
    ],
)
def test_two_sum_valid(arr: list[int], target: int, expected: list[int]):
    assert twoSum(arr, target) == expected


@pytest.mark.parametrize(
    "arr, target",
    [
        ([], -1),
        ([1], 1),
        ([1, 2], 8),
    ],
)
def test_two_sum_invalid(arr: list[int], target: int):
    with pytest.raises(ValueError):
        twoSum(arr, target)
