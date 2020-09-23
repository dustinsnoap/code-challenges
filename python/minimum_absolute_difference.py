# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

# Constraints:
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6

def minimumAbsDifference(arr):
    arr.sort(reverse=True)
    dct = {}
    min_distance = None
    while len(arr) > 1:
        n1 = arr.pop()
        n2 = arr[-1]
        diff = n2 - n1
        if diff not in dct: dct[diff] = [[n1,n2]]
        else: dct[diff].append([n1,n2])
        if min_distance is None or diff < min_distance: min_distance = diff

    return dct[min_distance]

inputs = [[4,2,1,3],[1,3,6,10,15],[3,8,-10,23,19,-4,-14,27]]
outputs = [[[1,2],[2,3],[3,4]],[[1,3]],[[-14,-10],[19,23],[23,27]]]

print("ATTEMPT 1")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if minimumAbsDifference(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")