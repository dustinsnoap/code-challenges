# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Follow up: Could you solve it without converting the integer to a string?

# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Example 4:
# Input: x = -101
# Output: false

# Constraints:
# -231 <= x <= 231 - 1

def solution1(x):
    if x < 0: return False
    nums = list(str(x))
    for i in range(len(nums)//2):
        if nums[i] == nums[-i-1]: continue
        return False
    return True

from tools import test
inputs = [121,-121,10,-101,1101011]
outputs = [True,False,False,False,True]
funcs = [solution1]

test(inputs,outputs,funcs)