package main
import "fmt"

//Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

//Example 1:
//s = "leetcode"
//return 0.

//Example 2:
//s = "loveleetcode",
//return 2.

//Note: You may assume the string contain only lowercase letters.

func firstUniqChar(s string) int {
	hash := make(map[rune][]int, len(s))
	for i, char := range s {
		if _, ok := hash[char]; ok {
			hash[char][1]++
		} else {
			hash[char] = []int{i, 1}
		}
	}
	lowest := -1
	for key := range hash{
		if hash[key][1] == 1 {
			if lowest == -1 || hash[key][0] < lowest {
				lowest = hash[key][0]
			}
		}
	}
	return lowest
}

func main() {
	ex1 := "leetcode" //0
	ex2 := "loveleetcode" //2
	ex3 := "dddccdbba" //8
	ex4 := "" //-1

	fmt.Println(firstUniqChar(ex1))
	fmt.Println(firstUniqChar(ex2))
	fmt.Println(firstUniqChar(ex3))
	fmt.Println(firstUniqChar(ex4))
}