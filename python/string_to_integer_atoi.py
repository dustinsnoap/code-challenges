# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
# Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
# and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, 
# which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, 
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Example 1:
# Input: str = "42"
# Output: 42

# Example 2:
# Input: str = "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.

# Example 3:
# Input: str = "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:
# Input: str = "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. 
# Therefore no valid conversion could be performed.

# Example 5:
# Input: str = "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.

# Example 6:
# Input: str = "3.14159"
# Output: 3

# Example 7:
# Input: str = "-+7"
# Output: 0

# Example 8:
# Input: str = ""
# Output: 0

# Example 9:
# Input: str = "+1"
# Output: 1

# Example 10:
# Input: str = "+-1"
# Output: -1

# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.


def solution1(s):
    if len(s) == 0: return 0
    valid = set(['1','2','3','4','5','6','7','8','9','0'])
    optional = set(['+','-'])
    for i,c in enumerate(s):
        if c != ' ':
            s = s[i:]
            break
    negative = False
    if s[0] in optional:
        if s[0] == '-': negative = True
        s = s[1:]
    string = []
    for c in s:
        if c in valid: string.append(c)
        else: break
    if len(string) > 0:
        num = int(''.join(string))
        if negative: num *= -1
        return min(2147483647,max(-2147483648,num))
    return 0



from tools import test
inputs = ['42','   -42','4193 with words','words and 987','-91283472332','3.14159','-+7',"",'+1','+-1']
outputs = [42,-42,4193,0,-2147483648,3,0,0,1,0]
funcs = [solution1]

test(inputs, outputs, funcs)