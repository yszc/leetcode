package main

import "fmt"
import "strings"
func wordPattern(pattern string, str string) bool {
    var dict [26]string
    var wdict map[string]rune
    wdict = make(map[string]rune)
    words := strings.Split(str, " ")
    if len(words) != len(pattern) {
        return false
    }
    for i,c := range pattern{
        if len(dict[c-97]) == 0 {
            dict[c-97] = words[i]
        }else if dict[c-97] != words[i] {
            return false
        }
        if wdict[words[i]] == 0 {
            wdict[words[i]] = c
        }else if wdict[words[i]] != c {
            return false
        }
    }
    return true
}
func main() {
    fmt.Println(wordPattern("abba", "dog dog dog dog"))
}
