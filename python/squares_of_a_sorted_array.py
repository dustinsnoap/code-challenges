# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Example 1:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Note:
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.

def sortedSquares(A):
    ans = [n**2 for n in A]
    ans.sort()
    return ans

inputs = [[-4,-1,0,3,10],[-7,-3,2,3,11]]
outputs = [[0,1,9,16,100],[4,9,9,49,121]]

# print("ATTEMPT 1")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if sortedSquares(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")