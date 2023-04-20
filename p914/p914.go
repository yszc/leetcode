package main

import "fmt"
func gcd(x, y int) int {
    tmp := x % y
	if tmp > 0 {
		return gcd(y, tmp)
	} else {
		return y
	}
}
func hasGroupsSizeX(deck []int) bool {
    var dict map[int]int
    var res int
    if len(deck) == 1 {
        return false
    }
    dict = make(map[int]int)
    for _, x := range deck {
        dict[x] = dict[x]+1
    }
    for key := range dict {
        if res == 0 {
            res = dict[key]
            goto judge
        }
        res = gcd(res, dict[key])
        judge: if res < 2 {
            return false
        }
    }
    return true
}
func main() {
    var nums = []int{1}
    fmt.Println(hasGroupsSizeX(nums))
}
