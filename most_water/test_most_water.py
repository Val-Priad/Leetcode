import pytest
from most_water.most_water import maxArea


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 7, 2, 5, 4, 7, 3, 6], 36),
        ([2, 2, 2], 4),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_most_water(arr: list[int], expected: int):
    assert maxArea(arr) == expected
