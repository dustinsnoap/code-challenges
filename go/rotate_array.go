package main
import "fmt"

//Given an array, rotate the array to the right by k steps, where k is non-negative.

//Example 1:

//Input: [1,2,3,4,5,6,7] and k = 3
//Output: [5,6,7,1,2,3,4]
//Explanation:
//rotate 1 steps to the right: [7,1,2,3,4,5,6]
//rotate 2 steps to the right: [6,7,1,2,3,4,5]
//rotate 3 steps to the right: [5,6,7,1,2,3,4]
//Example 2:

//Input: [-1,-100,3,99] and k = 2
//Output: [3,99,-1,-100]
//Explanation: 
//rotate 1 steps to the right: [99,-1,-100,3]
//rotate 2 steps to the right: [3,99,-1,-100]
//Note:

//Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
//Could you do it in-place with O(1) extra space?

func rotate(nums []int, k int) []int{
	if len(nums) == 1 || k == 0 {return []int{1,2,3}}
	temp := nums[0]
	start := 0
	for i := 0; i < len(nums); i++ {
		idx := ((i+1)*k + start) % len(nums)
		nums[idx], temp = temp, nums[idx]
		if idx == start {
			start = (start+1)%len(nums)
			temp = nums[start]
		}
	}
	return nums
}

func main() {
	ex1 := []int{1,2,3,4,5,6,7}
	ex2 := []int{-1,-100,3,99}
	ex3 := []int{1,2}
	fmt.Println(rotate(ex1, 3)) //[5 6 7 1 2 3 4]
	fmt.Println(rotate(ex2, 2)) //[3 99 -1 -100]
	fmt.Println(rotate(ex3, 3)) //[2 1]
}