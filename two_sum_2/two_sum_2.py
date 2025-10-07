"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""
# Algorithm with explicit elimination
# def twoSum(numbers: list[int], target: int) -> list[int]:
#     if not numbers or len(numbers) == 1:
#         raise ValueError
#     left_idx = 0
#     right_idx = len(numbers) - 1

#     while left_idx < right_idx:
#         while (
#             target - numbers[left_idx] > numbers[right_idx]
#             and left_idx < right_idx
#         ):
#             left_idx += 1

#         while (
#             target - numbers[left_idx] < numbers[right_idx]
#             and left_idx < right_idx
#         ):
#             right_idx -= 1

#         if numbers[left_idx] + numbers[right_idx] == target:
#             return [left_idx + 1, right_idx + 1]

#     raise ValueError


# Algorithm with implicit logic of elimination
def twoSum(numbers: list[int], target: int) -> list[int]:
    if not numbers or len(numbers) == 1:
        raise ValueError

    left_idx = 0
    right_idx = len(numbers) - 1

    while left_idx < right_idx:
        current_sum = numbers[left_idx] + numbers[right_idx]

        if current_sum == target:
            return [left_idx + 1, right_idx + 1]
        elif current_sum > target:
            right_idx -= 1
        else:
            left_idx += 1
    raise ValueError
