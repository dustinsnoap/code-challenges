# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hash: return [hash[compliment], i]
        hash[nums[i]] = i


ex1 = [2,7,11,15] #[0,1]
print(twoSum(ex1, 9))