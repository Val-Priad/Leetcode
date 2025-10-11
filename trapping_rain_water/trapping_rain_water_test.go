package trapping_rain_water

import (
	"testing"
)

func TestTrap(t *testing.T) {
	cases := []struct {
		name     string
		arr      []int
		expected int
	}{
		{"", []int{0, 2, 0, 3, 1, 0, 1, 3, 2, 1}, 9},
		{"", []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}, 6},
		{"", []int{4, 2, 0, 3, 2, 5}, 9},
		{"", []int{3, 0, 1, 0, 2}, 5},
	}

	for _, test := range cases {
		t.Run(test.name, func(t *testing.T) {
			got := trap(test.arr)
			if got != test.expected {
				t.Errorf("Expected -> %d, but got -> %v", test.expected, got)
			}
		})
	}

}
