# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example 1:
# Input: [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: [1,1]
# Output: [2]

# Example 3:
# Input: []
# Output: []

# Example 4:
# Input: [2,2]
# Output: [1]

def findDisappearedNumbers(nums):
    expected = set(list(range(1,len(nums)+1)))
    return list(expected.difference(set(nums)))

from tools import test
inputs = [[4,3,2,7,8,2,3,1],[1,1],[],[2,2],[1,1,2,2]]
outputs = [[5,6],[2],[],[1],[3,4]]
funcs = [findDisappearedNumbers]
test(inputs, outputs, funcs)