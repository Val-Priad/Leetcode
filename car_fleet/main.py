"""https://leetcode.com/problems/car-fleet/description/"""


def merge(left_array, right_array):
    array = [0] * (len(left_array) + len(right_array))
    idx = left_idx = right_idx = 0

    while left_idx < len(left_array) and right_idx < len(right_array):
        if left_array[left_idx][0] > right_array[right_idx][0]:
            array[idx] = left_array[left_idx]
            left_idx += 1
        else:
            array[idx] = right_array[right_idx]
            right_idx += 1
        idx += 1
    while left_idx < len(left_array):
        array[idx] = left_array[left_idx]
        left_idx += 1
        idx += 1
    while right_idx < len(right_array):
        array[idx] = right_array[right_idx]
        right_idx += 1
        idx += 1

    return array


def merge_sort_cars(array):
    if len(array) <= 1:
        return array

    left_array = merge_sort_cars(array[: len(array) // 2])
    right_array = merge_sort_cars(array[len(array) // 2 :])

    return merge(left_array, right_array)


def car_fleet(target: int, position: list[int], speed: list[int]):
    cars = sorted([[a, b] for a, b in zip(position, speed)])[::-1]
    last = -1
    cur = 0
    counter = 0
    for p, s in cars:
        cur = (target - p) / s
        if cur <= last:
            counter -= 1
            cur = last
        last = cur
        counter += 1
    return counter


print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # must be 3
