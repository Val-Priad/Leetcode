package valid_palindrome

import (
	"testing"
)

func TestIsValidPalindrome(t *testing.T) {
	cases := []struct {
		name string
		s    string
		want bool
	}{
		{"Long str 1", "Was it a car or a cat I saw?", true},
		{"Long str 2", "A man, a plan, a canal: Panama", true},
		{"empty string", "", true},
		{"string with whitespaces", " ", true},
		{"one character", "a", true},
		{"dot with coma", ".,", true},
		{"not a palindrome", "race a car", false},
		{"number with char", "0P", false},
	}

	for _, value := range cases {
		t.Run(value.name, func(t *testing.T) {
			got := isPalindrome(value.s)
			if got != value.want {
				t.Errorf("isPalindrome(%q) = %v; want %v", value.s, got, value.want)
			}
		})
	}
}
