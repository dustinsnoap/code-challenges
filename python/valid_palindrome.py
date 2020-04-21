# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

import re

def isPalindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]
    

ex1 = "A man, a plan, a canal: Panama" #true
ex2 = "arace a car" #false

print(isPalindrome(ex1))
print(isPalindrome(ex2))