# Given an array nums containing n distinct numbers taken from 0, 1, 2, ..., n, return the one that is missing from the array.
# Follow up: Could you implement a solution using only constant extra space complexity and linear runtime complexity?

# Example 1:
# Input: nums = [3,0,1]
# Output: 2

# Example 2:
# Input: nums = [0,1]
# Output: 2

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

# Example 4:
# Input: nums = [0]
# Output: 1

# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

def missingNumber(nums):
    expected = [None] * (len(nums)+1)
    for n in nums: expected[n] = n
    for i in range(len(expected)):
        if expected[i] == None: return i
    return False

def missingNumber2(nums):
    return set([n for n in range(len(nums)+1)]).difference(set(nums)).pop()

from tools import test
inputs = [[3,0,1],[0,1],[9,6,4,2,3,5,7,0,1],[0]]
outputs = [2,2,8,1]
funcs = [missingNumber,missingNumber2]

test(inputs, outputs, funcs)