# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def solution1(s):
    opposite = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    closing_stack = []
    for bracket in s:
        if bracket in opposite: closing_stack.append(opposite[bracket])
        else:
            try: 
                if bracket != closing_stack.pop(): return False
            except: return False
    return len(closing_stack) == 0

def solution2(s):
    stack = []
    dct = {')':'(',']':'[','}':'{'}
    for c in s:
        if c in dct.values(): stack.append(c)
        elif c in dct:
            if len(stack) == 0 or dct[c] != stack.pop(): return False
        else: return False
    return stack == []


from tools import test
inputs = ['()','()[]{}','(]','([)]','{[]}','[',']','){']
outputs = [True,True,False,False,True,False,False,False]
funcs = [solution1,solution2]

test(inputs, outputs, funcs)