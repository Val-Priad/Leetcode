// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
package two_sum_2

import "fmt"

func twoSum(numbers []int, target int) ([2]int, error) {
	leftIdx := 0
	rightIdx := len(numbers) - 1

	for leftIdx < rightIdx {
		currentSum := numbers[leftIdx] + numbers[rightIdx]
		if currentSum == target {
			return [2]int{leftIdx + 1, rightIdx + 1}, nil
		} else if currentSum > target {
			rightIdx--
		} else {
			leftIdx++
		}
	}

	return [2]int{}, fmt.Errorf("Invalid input couldn't find result")
}
