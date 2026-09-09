package main

import "fmt"

func countCommas(n int) int {
	if n < 1000 {
		return 0
	}

	return n - 999
}

func main() {
	result := countCommas(1002)
	fmt.Println(result)
}