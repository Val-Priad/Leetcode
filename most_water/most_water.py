"""https://leetcode.com/problems/container-with-most-water/description/"""


def maxArea(heights: list[int]) -> int:
    left_idx = 0
    right_idx = len(heights) - 1
    max_area = 0
    while left_idx < right_idx:
        left_height = heights[left_idx]
        right_height = heights[right_idx]

        area = (right_idx - left_idx) * min(left_height, right_height)
        if area > max_area:
            max_area = area

        if left_height <= right_height:
            left_idx += 1
        else:
            right_idx -= 1

    return max_area
