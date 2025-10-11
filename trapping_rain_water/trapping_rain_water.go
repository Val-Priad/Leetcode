package trapping_rain_water

// func trap(heights []int) int {
// 	leftMax := 0
// 	rightMax := 0
// 	prefixes := []int{}
// 	suffixes := []int{}
// 	minAr := []int{}
// 	collectedWater := 0

// 	for i := 0; i < len(heights); i++ {
// 		j := len(heights) - 1 - i
// 		prefixes = append(prefixes, leftMax)
// 		suffixes = append(suffixes, rightMax)
// 		leftMax = max(leftMax, heights[i])
// 		rightMax = max(rightMax, heights[j])
// 	}

// 	for i := 0; i < len(heights); i++ {
// 		j := len(heights) - 1 - i
// 		minAr = append(minAr, min(prefixes[i], suffixes[j]))
// 	}

// 	for i := 0; i < len(heights); i++ {
// 		waterLevel := minAr[i] - heights[i]
// 		if waterLevel > 0 {
// 			collectedWater += waterLevel
// 		}
// 	}

// 	return collectedWater
// }

func trap(heights []int) int {
	leftIdx := 0
	rightIdx := len(heights) - 1
	leftMax := heights[leftIdx]
	rightMax := heights[rightIdx]
	collectedWater := 0

	for leftIdx < rightIdx {
		if leftMax < rightMax {
			collectedWater += leftMax - heights[leftIdx]
			leftIdx += 1
			leftMax = max(leftMax, heights[leftIdx])
		} else {
			collectedWater += rightMax - heights[rightIdx]
			rightIdx -= 1
			rightMax = max(rightMax, heights[rightIdx])
		}

	}

	return collectedWater
}
