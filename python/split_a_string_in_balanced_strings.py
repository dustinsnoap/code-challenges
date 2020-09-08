# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

# Constraints:
# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'

def balancedStringSplit(s):
    counter = 0
    leftcount = 0
    rightcount = 0
    for c in s:
        if c is not subletter:
            subletter = c
        if c == 'L': leftcount += 1
        else: rightcount += 1
        if leftcount == rightcount:
            leftcount = 0
            rightcount = 0
            counter += 1
    return counter

def balancedStringSplit2(s):
    total = 0
    counter = 0
    for c in s:
        if c == 'L': counter += 1
        else: counter -= 1
        if counter == 0:
            total += 1
    return total

examples = ["RLRRLLRLRL","RLLLLRRRLR","LLLLRRRR","RLRRRLLRLL"]
answers = [4,3,1,2]

for idx, num in enumerate(examples):
    print('guess:', balancedStringSplit2(num), 'ans:', answers[idx])


