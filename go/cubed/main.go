package main

import (
	"math"
)

func SumCubes(n int) {
	// your code here
	var cubes []int
	for i := 0; i < n; i++ {
		cubes = append(math.Cbrt(i))
	}
}

func main() {
	SumCubes(2)
}
