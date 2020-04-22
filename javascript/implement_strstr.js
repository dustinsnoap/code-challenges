// Implement strStr().
// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Example 1:
// Input: haystack = "hello", needle = "ll"
// Output: 2

// Example 2:
// Input: haystack = "aaaaa", needle = "bba"
// Output: -1

// Clarification:
// What should we return when needle is an empty string? This is a great question to ask during an interview.
// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

const strStr = (haystack, needle) => {
    if(!needle) return 0
    for(let i=0; i<haystack.length; i++) {
        if(needle == haystack.substring(i, i+needle.length))
            return i
    }
    return -1
}

const ex1 = ['hello', 'll'] //2
const ex2 = ['aaaaa', 'bba'] //-1
const ex3 = ['farts', ''] //0

console.log(strStr(ex1[0], ex1[1]))
console.log(strStr(ex2[0], ex2[1]))
console.log(strStr(ex3[0], ex3[1]))