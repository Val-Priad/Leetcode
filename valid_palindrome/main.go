// https://leetcode.com/problems/valid-palindrome/

package main

import (
	"unicode"
)

func isPalindrome(s string) bool {
	if len(s) == 0 {
		return true
	}

	leftIdx := 0
	rightIdx := len(s) - 1

	for leftIdx < rightIdx {
		for leftIdx < rightIdx && !isAlphaNum(rune(s[leftIdx])) {
			leftIdx++
		}
		for rightIdx > leftIdx && !isAlphaNum(rune(s[rightIdx])) {
			rightIdx--
		}

		if unicode.ToLower(rune(s[leftIdx])) != unicode.ToLower(rune(s[rightIdx])) {
			return false
		}

		leftIdx++
		rightIdx--
	}

	return true
}

func isAlphaNum(c rune) bool {
	return (int(c) >= int('a') && int(c) <= int('z') ||
		int(c) >= int('A') && int(c) <= int('Z') ||
		int(c) >= int('0') && int(c) <= int('9'))
}

func main() {
}
