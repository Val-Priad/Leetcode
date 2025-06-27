def merge(left_array: list[int], right_array: list[int]):
    array = [0] * (len(left_array) + len(right_array))
    left_idx = 0
    right_idx = 0
    idx = 0
    while left_idx < len(left_array) and right_idx < len(right_array):
        if left_array[left_idx] < right_array[right_idx]:
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


def merge_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    left_array = merge_sort(array[: len(array) // 2])
    right_array = merge_sort(array[len(array) // 2 :])
    
    return merge(left_array, right_array)


arr_t = [15, 22, -5, -5, 4, 3]
print(merge_sort(arr_t))
