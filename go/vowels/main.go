package main

import "fmt"

func Solve(s string) int {

	vowels := map[string]int{
		"a": 0,
		"e": 0,
		"i": 0,
		"o": 0,
		"u": 0,
	}

	for i := 0; i < len(s); i++ {
		char := string(s[i])

		fmt.Println(char)
		if _, ok := vowels[char]; ok {
			vowels[char]++
		}

	}
	return 0
}

func main() {
	Solve("codewarriors")

}
