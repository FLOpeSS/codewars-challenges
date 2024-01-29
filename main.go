package main

import "fmt"

func bubble_sort(array []int) []int {
	for i := 0; i < len(array); i++ {
		for j := i + 1; j < len(array); j++ {
			if array[j] < array[i] {
				tmp := array[i]
				array[i] = array[j]
				array[j] = tmp
			}
		}
	}
	return array
}

func main() {
	fmt.Println("hello world")
}
