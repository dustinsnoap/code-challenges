package main
import "fmt"

//Given a non-empty array of integers, every element appears twice except for one. Find that single one.

//Note:
//Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

//Example 1:
//Input: [2,2,1]
//Output: 1

//Example 2:
//Input: [4,1,2,1,2]
//Output: 4

// #Explanation:
//^= is the XOR opporator
//any number XOR 0 is the same number
//any number XOR itself is 0
//if we XOR every number together only the odd one out should remain

func singleNumber(nums []int) int {
	bit := 0
	for i := 0; i < len(nums); i++ {bit ^= nums[i]}
	return bit
}

func main() {
	ex1 := []int{2,2,1}
	ex2 := []int{4,1,2,1,2}
	fmt.Println(singleNumber(ex1))
	fmt.Println(singleNumber(ex2))
}