package main

import "fmt"

func Divisors(n int) {
	//Put your code here
	var divisors []int
	for i := 1; i < n; i++ {
		divisors = append(divisors, n/i)
		// fmt.Println(oper)
	}
	fmt.Println(divisors)
}

func isInt(value interface{}) bool {
	switch value.(type) {
	case int, int8, int16, int32, int64:
		return true
	default:
		return false
	}
}

func main() {
	// if isInt(4 / 3) {
	// 	fmt.Println("is an integer")
	// } else {
	// 	fmt.Println("is not a integer")
	// }
	fmt.Println(4 / 3)
	Divisors(4)
	Divisors(5)
	Divisors(12)
}
