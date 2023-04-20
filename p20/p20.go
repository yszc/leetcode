package main

import (
    "fmt"
    "strings"
)
type Stack struct {
    st []rune
    top int
}

func (s *ItemStack) New() *ItemStack {
	s.items = []Item{}
	return s
}

func (s Stack) Push(c rune){
    s.st = append(s.st, c)
}

func (s Stack) Pop() rune {
    if s.top < 0 {
        return -1
    }
    t := s.st[s.top]
    delete(s.st, s.top)
    return t
}

func (s Stack) Top() rune {
    if s.top < 0 {
        return -1
    }
    return s.st[s.top]
}

func isValid(s string) bool {

    top := -1
    if len(s) == 0 {
        return true
    }
    for _,c := range s {
        if strings.ContainsRune('{[(', c) {

        }
    }
}
func main() {
    s := "()[]{}"
    fmt.Println(isValid(s))
}
