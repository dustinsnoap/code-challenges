package main

import "fmt"

func removeDuplicates(nums []int) int {
	var curr int = 1
	for i := 1; i < len(nums); i++ {
		if nums[i-1] != nums[i] {
			nums[curr] = nums[i]
			curr++
		}
	}
	return curr
}

func main() {
	ex1 := []int{1,1,2}
	ex2 := []int{0,0,1,1,1,2,2,3,3,4}
	fmt.Println(removeDuplicates(ex1))
	fmt.Println(removeDuplicates(ex2))
}