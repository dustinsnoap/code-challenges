// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

// Note: For the purpose of this problem, we define empty string as valid palindrome.

// Example 1:
// Input: "A man, a plan, a canal: Panama"
// Output: true

// Example 2:
// Input: "race a car"
// Output: false

isPalindrome = s => {
    s = s.toLowerCase().replace(/[^a-z0-9]/g, '')
    const r = s.split('').reverse().join('')
    return r == s
}

const ex1 = "A man, a plan, a canal: Panama" //true
const ex2 = "arace a car" //false

console.log(isPalindrome(ex1))
console.log(isPalindrome(ex2))