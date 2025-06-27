package main

import (
	"fmt"
)

func merge(leftArray []int, rightArray []int) []int {
	array := make([]int, len(leftArray)+len(rightArray))
	leftIdx := 0
	rightIdx := 0
	idx := 0

	for leftIdx < len(leftArray) && rightIdx < len(rightArray) {
		if leftArray[leftIdx] < rightArray[rightIdx] {
			array[idx] = leftArray[leftIdx]
			leftIdx++
		} else {
			array[idx] = rightArray[rightIdx]
			rightIdx++
		}
		idx++
	}

	for leftIdx < len(leftArray) {
		array[idx] = leftArray[leftIdx]
		leftIdx++
		idx++
	}

	for rightIdx < len(rightArray) {
		array[idx] = rightArray[rightIdx]
		rightIdx++
		idx++
	}
	return array
}

func mergeSort(array []int) []int {
	if len(array) <= 1 {
		return array
	}

	leftArray := mergeSort(array[:len(array)/2])
	rightArray := mergeSort(array[len(array)/2:])

	return merge(leftArray, rightArray)
}

func main() {
	testSlice := []int{13, 12, -5, 18, 22, 7, 6, 9, -4}
	fmt.Printf("%v", mergeSort(testSlice))
}
