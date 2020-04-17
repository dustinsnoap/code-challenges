package main
import "fmt"

//Given a non-empty array of digits representing a non-negative integer, 
//plus one to the integer.
//The digits are stored such that the most significant digit is at the head of the list,
//and each element in the array contain a single digit.
//You may assume the integer does not contain any leading zero, 
//except the number 0 itself.

//Example 1:
//Input: [1,2,3]
//Output: [1,2,4]
//Explanation: The array represents the integer 123.

//Example 2:
//Input: [4,3,2,1]
//Output: [4,3,2,2]
//Explanation: The array represents the integer 4321.

func plusOne(digits []int) []int {
	for i := len(digits)-1; i>=0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	if digits[0] == 0 {digits = append([]int{1}, digits...)}
	return digits
}

func main() {
	ex1 := []int{1,2,3} //[1 2 4]
	ex2 := []int{4,3,2,1} //[4 3 2 2]
	fmt.Println(plusOne(ex1))
	fmt.Println(plusOne(ex2))
}