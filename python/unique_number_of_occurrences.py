# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
# Accepted

def uniqueOccurrences(arr):
    dct = {}
    for n in arr:
        if n in dct: dct[n] += 1
        else: dct[n] = 1
    
    count_dct = {}
    for e in dct:
        if dct[e] in count_dct: return False
        count_dct[dct[e]] = 1
        
    return True

test = [1,2,2,1,1,3]
print(uniqueOccurrences(test))

inputs = [[1,2,2,1,1,3],[1,2],[-3,0,1,-3,1,1,1,-3,10,0]]
outputs = [True,False,True]

print("ATTEMPT 1")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if uniqueOccurrences(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")