package main

import (
	"fmt"
)

func merge(leftArray [][2]int, rightArray [][2]int) [][2]int {
	array := make([][2]int, len(leftArray)+len(rightArray))

	leftIdx, rightIdx, idx := 0, 0, 0
	for leftIdx < len(leftArray) && rightIdx < len(rightArray) {
		if leftArray[leftIdx][0] > rightArray[rightIdx][0] {
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

func mergeSort(array [][2]int) [][2]int {
	if len(array) <= 1 {
		return array
	}
	leftArray := mergeSort(array[:len(array)/2])
	rightArray := mergeSort(array[len(array)/2:])

	return merge(leftArray, rightArray)
}

func carFleet(target int, position []int, speed []int) int {
	cars := make([][2]int, len(position))
	for i := range position {
		cars[i][0] = position[i]
		cars[i][1] = speed[i]
	}
	cars = mergeSort(cars)
	p, s, counter, cur, last := 0, 0, 0, 0.0, -1.0

	for _, car := range cars {
		p, s = car[0], car[1]
		cur = float64(target-p) / float64(s)
		if cur <= last {
			counter--
			cur = last
		}
		last = cur
		counter++
	}
	return counter
}

func main() {
	fmt.Printf("%v", carFleet(10, []int{6, 8}, []int{3, 2}))
}
