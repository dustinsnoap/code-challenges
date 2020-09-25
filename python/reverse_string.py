# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverseString(s):
    s[:] = s[::-1]
    return s

def reverseString2(s):
    s = s[::-1]
    return s

inputs = [["h","e","l","l","o"],["H","a","n","n","a","h"]]
outputs = [["o","l","l","e","h"],["h","a","n","n","a","H"]]

print("ATTEMPT 1")
test_input = [a[:] for a in inputs]
for idx in range(len(test_input)):
    test_num = idx + 1
    result = "Success" if reverseString(test_input[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")

print("ATTEMPT 2")
test_input = [a[:] for a in inputs]
for idx in range(len(test_input)):
    test_num = idx + 1
    result = "Success" if reverseString2(test_input[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")