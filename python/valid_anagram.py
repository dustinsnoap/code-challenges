# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

def isAnagram(s, t):
    if len(s) != len(t): return False
    chars = {}
    for i in range(len(s)):
        if s[i] not in chars: chars[s[i]] = 1
        else: chars[s[i]] += 1
        if t[i] not in chars: chars[t[i]] = -1
        else: chars[t[i]] -= 1
    for char in chars:
        if chars[char] != 0: return False
    return True

def isAnagram2(s, t):
    if len(s) != len(t): return False
    ss = {}
    ts = {}
    for i in range(len(s)):
        if s[i] not in ss: ss[s[i]] = 1
        else: ss[s[i]] += 1
        if t[i] not in ts: ts[t[i]] = 1
        else: ts[t[i]] += 1
    return ss == ts


inputs = [{'s': "anagram", 't': "nagaram"}, {'s': "rat", 't': "car"}]
outputs = [True, False]

for i in inputs:
    print(isAnagram2(s=i['s'], t=i['t']))