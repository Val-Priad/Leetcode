import pytest
from trapping_rain_water.trapping_rain_water import trap


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([3, 0, 1, 0, 2], 5),
    ],
)
def test_trapping_rain_water(arr: list[int], expected: int):
    assert trap(arr) == expected
