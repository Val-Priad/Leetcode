// https://leetcode.com/problems/3sum/description/
package three_sum

import (
	"slices"
)

func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}

	slices.SortFunc(nums, func(a, b int) int {
		if a < b {
			return -1
		} else if a > b {
			return 1
		} else {
			return 0
		}
	})

	results := [][]int{}

	for idx, num := range nums {
		if idx > 0 && num == nums[idx-1] {
			continue
		}
		leftIdx := idx + 1
		rightIdx := len(nums) - 1

		for leftIdx < rightIdx {
			total := num + nums[leftIdx] + nums[rightIdx]

			if total > 0 {
				rightIdx--
			} else if total < 0 {
				leftIdx++
			} else {
				results = append(results, []int{num, nums[leftIdx], nums[rightIdx]})
				processedNum := nums[leftIdx]
				for nums[leftIdx] == processedNum && leftIdx < rightIdx {
					leftIdx++
				}
			}

		}
	}

	return results
}
