package main
import "fmt"

//Given an array of integers, return indices of the two numbers such that they add up to a specific target.

//You may assume that each input would have exactly one solution, and you may not use the same element twice.

//Example:
//Given nums = [2, 7, 11, 15], target = 9,
//Because nums[0] + nums[1] = 2 + 7 = 9,
//return [0, 1].

func twoSum(nums []int, target int) []int {
	hash := make(map[int]int, len(nums))
	for i:=0; i<len(nums); i++ {
		compliment := target - nums[i]
		if c_idx, ok := hash[compliment]; ok {
			return []int{c_idx, i}
		}
		hash[nums[i]] = i
	}
	return nil
}

func main() {
	ex1 := []int{2,7,11,15}
	fmt.Println(twoSum(ex1, 9))
}