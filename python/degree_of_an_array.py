# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

# Example 3:
# Input: nums = [1,2,2,1,2,1,1,1,1,2,2,2]
# Output: 9

# Constraints:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

def findShortestSubArray(nums):
    dct = {}
    for i,n in enumerate(nums):
        if n not in dct: dct[n] = [i-1,1,i]
        else:
            dct[n][1] += 1
            dct[n][2] = i
    max = 0
    degree = 99999
    for n in dct:
        if dct[n][1] == max:
            if dct[n][2]-dct[n][0] < degree: degree = dct[n][2]-dct[n][0]
        elif dct[n][1] > max:
            max = dct[n][1]
            degree = dct[n][2]-dct[n][0]
    return degree


from tools import test
inputs = [[1,2,2,3,1],[1,2,2,3,1,4,2],[1,2,2,1,2,1,1,1,1,2,2,2]]
outputs = [2,6,9]
funcs = [findShortestSubArray]

test(inputs, outputs, funcs)