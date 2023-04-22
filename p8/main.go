package main

// @ai write a golang function named myAtoi, arguments: s string, return s without space char and convert it to unsigned integer

import (
	"fmt"
	"strings"
)

func myAtoi(s string) int {
	s = strings.TrimSpace(s)
	if len(s) == 0 {
		return 0
	}
	var sign int
	if s[0] == '-' {
		sign = -1
		s = s[1:]
	} else if s[0] == '+' {
		sign = 1
		s = s[1:]
	} else {
		sign = 1
	}
	var num int
	for i := 0; i < len(s); i++ {
		if s[i] < '0' || s[i] > '9' {
			break
		}
		num = num*10 + int(s[i]-'0')
		if num > 2147483647 {
			if sign == 1 {
				return 2147483647
			} else {
				return -2147483648
			}
		}
	}
	return num * sign
}

func main() {
	fmt.Println(myAtoi("-123a"))
}
