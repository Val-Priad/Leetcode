"""https://leetcode.com/problems/3sum/description/"""


def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []

    nums.sort()

    results: list[list[int]] = []

    for idx, num in enumerate(nums):
        left_idx = idx + 1
        right_idx = len(nums) - 1

        # idx > 0 is used to not receive last element
        # during the firs iteration
        if idx > 0 and num == nums[idx - 1]:
            continue

        while left_idx < right_idx:
            total = nums[left_idx] + nums[right_idx] + num
            if total > 0:
                right_idx -= 1
            elif total < 0:
                left_idx += 1
            else:
                results.append([num, nums[left_idx], nums[right_idx]])
                processed_num = nums[left_idx]
                while nums[left_idx] == processed_num and left_idx < right_idx:
                    left_idx += 1

    return results
