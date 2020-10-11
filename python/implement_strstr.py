# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

# Constraints:
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.

def solution0(haystack, needle):
    if not needle: return 0
    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:
            return i
    return -1

def solution1(haystack, needle):
    if needle == '': return 0
    needle_len = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+needle_len] == needle: return i
    return -1

inputs = [['hello', 'll'],['aaaa','bba'],['','']]
outputs = [2,-1,0]
funcs = [solution0, solution1]

for idx, func in enumerate(funcs):
    print(f'Solution {idx}')
    for i, input in enumerate(inputs):
        res = func(input[0],input[1])
        if res == outputs[i]: print('pass')
        else: print('fail')