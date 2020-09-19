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
        r = 0
        l = 0
        count = 0
        for c in s:
            if c == "R": r = r+1
            else: l = l+1
            if r == l:
                count = count + 1
                r = 0
                l = 0
        return count

def balancedStringSplit2(s):
        count = total = 0
        for c in s:
            if c == "R": count = count + 1
            else: count = count - 1
            if count == 0:
                total = total + 1
        return total
def balancedStringSplit3(s):
    dct = { 'L' : -1, 'R' : 1 }
    count = total = 0
    for char in s:
        count += dct[char]
        if count == 0:
            total += 1
    return total

inputs = ["RLRRLLRLRL","RLLLLRRRLR","LLLLRRRR","RLRRRLLRLL"]
outputs = [4,3,1,2]

print("ATTEMPT 1")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if balancedStringSplit(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")

print("ATTEMPT 2")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if balancedStringSplit2(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")

print("ATTEMPT 3")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if balancedStringSplit3(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")