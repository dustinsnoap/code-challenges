# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def solution1(nums, target):
    hash = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hash: return [hash[compliment], i]
        hash[nums[i]] = i

def solution2(nums, target):
    dct = {}
    for i, n in enumerate(nums):
        if n in dct: return [dct[n],i]
        dct[target-n] = i
    return False

inputs = [[[2,7,11,15],9],[[3,2,4],6],[[3,3],6]]
outputs = [[0,1],[1,2],[0,1]]
funcs = [solution1, solution2]

for j,func in enumerate(funcs):
    print("Solution", j)
    for idx, i in enumerate(inputs):
        out = func(i[0],i[1])
        if out == outputs[idx]: print("Pass")
        else: print("Fail")