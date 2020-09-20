# Given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.

# Constraints:
# 1 <= num <= 10^4
# num's digits are 6 or 9.

def maximum69Number(num):
    can_flip = True
    number = ''
    for n in str(num):
        if can_flip and n == '6':
            number += '9'
            can_flip = False
        else: number += n
    return int(number)

def maximum69Number2(num):
    nums = list(str(num))
    for i in range(len(nums)):
        if nums[i] == '6':
            nums[i] = '9'
            return int(''.join(nums))
    return num

inputs = [9669,9996,9999]
outputs = [9969,9999,9999]

print("ATTEMPT 1")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if maximum69Number(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")

print("ATTEMPT 2")
for idx in range(len(inputs)):
    test_num = idx + 1
    result = "Success" if maximum69Number2(inputs[idx]) == outputs[idx] else "Fail"
    print(f"test {test_num}: {result}")