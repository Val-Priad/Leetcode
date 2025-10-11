"""https://leetcode.com/problems/trapping-rain-water/"""
# def trap(heights: list[int]) -> int:
#     prefix_max: list[int] = [0] * len(heights)
#     suffix_max: list[int] = [0] * len(heights)
#     min_ar: list[int] = [0] * len(heights)
#     res: list[int] = []
#     left_max = 0
#     right_max = 0

#     for i in range(len(heights)):
#         j = -1 - i
#         prefix_max[i] = left_max
#         suffix_max[j] = right_max
#         left_max = max(heights[i], left_max)
#         right_max = max(heights[j], right_max)

#     for i in range(len(heights)):
#         min_ar[i] = min(prefix_max[i], suffix_max[i])

#     for i in range(len(heights)):
#         water_level = min_ar[i] - heights[i]
#         if water_level > 0:
#             res.append(water_level)

#     return sum(res)


# def trap(heights: list[int]) -> int:
#     prefix_max: list[int] = []
#     suffix_max: list[int] = []
#     min_ar: list[int] = []
#     res: int = 0
#     left_max = 0
#     right_max = 0

#     for i in range(len(heights)):
#         j = -1 - i
#         prefix_max.append(left_max)
#         suffix_max.append(right_max)
#         left_max = max(heights[i], left_max)
#         right_max = max(heights[j], right_max)

#     for i in range(len(heights)):
#         j = -1 - i
#         min_ar.append(min(prefix_max[i], suffix_max[j]))

#     for i in range(len(heights)):
#         water_level = min_ar[i] - heights[i]
#         if water_level > 0:
#             res += water_level

#     return res


def trap(heights: list[int]) -> int:
    leftIdx = 0
    rightIdx = len(heights) - 1
    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]
    collected_water = 0

    while leftIdx < rightIdx:
        if leftMax < rightMax:
            leftIdx += 1
            leftMax = max(leftMax, heights[leftIdx])
            # leftMax > heights[leftIdx] so ⬇️ can't be negative
            collected_water += leftMax - heights[leftIdx]
        else:
            rightIdx -= 1
            rightMax = max(rightMax, heights[rightIdx])
            collected_water += rightMax - heights[rightIdx]

    return collected_water
