# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [0]
# Output: 0

# Example 4:
# Input: nums = [-1]
# Output: -1

# Example 5:
# Input: nums = [-2147483647]
# Output: -2147483647

# Constraints:
# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1

def solution1(nums):
    current = 0
    greatest = nums[0]
    for n in nums:
        current = max(current+n,n)
        greatest = max(current,greatest)
        print('n', n, 'c', current, 'm', greatest)
    return greatest

def solution2(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1] if nums[i-1] > 0 else 0
    return max(nums)

from tools import test

inputs = [[-2,1,-3,4,-1,2,1,-5,4],[1],[0],[-1],[-2147483647]]
outputs = [6,1,0,-1,-2147483647]
funcs = [solution1, solution2]

test(inputs, outputs, funcs)