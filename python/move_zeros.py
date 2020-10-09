# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
        zeros = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] is 0:
                nums.pop(idx)
                zeros += 1
            else: idx += 1
        nums += [0]*zeros