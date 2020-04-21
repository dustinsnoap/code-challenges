// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

// Note: For the purpose of this problem, we define empty string as valid palindrome.

// Example 1:
// Input: "A man, a plan, a canal: Panama"
// Output: true

// Example 2:
// Input: "race a car"
// Output: false

package main
import (
	"fmt"
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	//clean up string
	s = strings.ToLower(s)
	reg, _ := regexp.Compile("[^a-z0-9]")
	s = reg.ReplaceAllString(s, "")
	//reverse clean solution
	r := ""
	for _,c := range s {
		r = string(c) + r
	}
	return r == s
}

func main() {
	ex1 := "A man, a plan, a canal: Panama" //true
	ex2 := "arace a car" //false

	fmt.Println(isPalindrome(ex1))
	fmt.Println(isPalindrome(ex2))
}