//Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

//Example 1:
//s = "leetcode"
//return 0.

//Example 2:
//s = "loveleetcode",
//return 2.

//Note: You may assume the string contain only lowercase letters.

const firstUniqChar = s => {
    let hash = {}
    for(let i=0; i<s.length; i++) {
        if(s[i] in hash) hash[s[i]][1]++
        else hash[s[i]] = [i,1]
    }
    for(const char in hash)
        if(hash[char][1] == 1) return hash[char][0]
    return -1
}

let ex1 = "leetcode"
let ex2 = "loveleetcode"
let ex3 = "dddccdbba"

console.log(firstUniqChar(ex1))
console.log(firstUniqChar(ex2))
console.log(firstUniqChar(ex3))