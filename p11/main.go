package main

import (
	"fmt"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func maxArea(height []int) int {
	var max_area, left, right int
	max_area = 0
	left = 0
	right = len(height) - 1
	for left < right {
		if max_area < min(height[left], height[right])*(right-left) {
			max_area = min(height[left], height[right]) * (right - left)
		}
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return max_area
}

func main() {
	primes := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(primes))
}
