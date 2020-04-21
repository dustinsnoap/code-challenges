# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Example 1:
# s = "leetcode"
# return 0.

# Example 2:
# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.

def firstUniqChar(s):
    hash = {}
    for i in range(len(s)):
        if s[i] in hash: hash[s[i]][1] += 1
        else: hash[s[i]] = [i,1]
    for item in hash:
        if hash[item][1] == 1: return hash[item][0]
    return -1

ex1 = "leetcode"
ex2 = "loveleetcode"
ex3 = "dddccdbba"

print(firstUniqChar(ex1))
print(firstUniqChar(ex2))
print(firstUniqChar(ex3))