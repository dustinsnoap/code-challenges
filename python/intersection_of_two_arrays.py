# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:
# Each element in the result must be unique.
# The result can be in any order.

def intersection(nums1, nums2):
    out = []
    dct = {}
    for n in nums1:
        dct[n] = True
    for n in nums2:
        if n in dct:
            dct.pop(n)
            out.append(n)
    return out

inputs = [[[1,2,2,1],[2,2]],[[4,9,5],[9,4,9,8,4]]]
outputs = [[2],[9,4]]

print("ATTEMPT 1")
test_input = [a[:] for a in inputs]
for idx in range(len(test_input)):
    test_num = idx + 1
    result = "Success" if intersection(test_input[idx][0],test_input[idx][1]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")