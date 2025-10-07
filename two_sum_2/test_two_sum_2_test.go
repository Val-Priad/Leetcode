package two_sum_2

import (
	"testing"
)

func TestTwoSumValid(t *testing.T) {
	cases := []struct {
		message  string
		arr      []int
		target   int
		expected [2]int
	}{
		{"normal", []int{2, 7, 11, 15}, 9, [2]int{1, 2}},
		{"normal", []int{2, 3, 4}, 6, [2]int{1, 3}},
		{"normal", []int{-1, 0}, -1, [2]int{1, 2}},
		{"normal", []int{3, 24, 50, 79, 88, 150, 345}, 200, [2]int{3, 6}},
	}

	for _, test := range cases {
		t.Run(test.message, func(t *testing.T) {
			got, _ := twoSum(test.arr, test.target)
			want := test.expected
			if got != want {
				t.Errorf("Test failed for input %v, the output was %v, want %v", test.arr, got, want)
			}
		})

	}
}

func TestTwoSumInvalid(t *testing.T) {
	cases := []struct {
		message string
		arr     []int
		target  int
	}{
		{"fail", []int{1, 2}, 8},
	}

	for _, test := range cases {
		t.Run(test.message, func(t *testing.T) {
			got, err := twoSum(test.arr, test.target)
			if err == nil {
				t.Errorf("%s: expected an error, but got result %v", test.message, got)
			}
		})

	}
}
