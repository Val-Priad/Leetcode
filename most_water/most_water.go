// https://leetcode.com/problems/container-with-most-water/description/
package most_water

func maxArea(heights []int) int {
	i := 0
	j := len(heights) - 1
	areaMax := 0

	for i < j {
		area := (j - i) * min(heights[i], heights[j])
		if area > areaMax {
			areaMax = area
		}

		if heights[i] <= heights[j] {
			i++
		} else {
			j--
		}
	}
	return areaMax
}
