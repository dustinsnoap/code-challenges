# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

def solution1(n):
    if n < 4: return n
    n1 = 2
    n2 = 3
    for num in range(4,n+1):
        n1, n2 = n2, n1 + n2
    return n2

from tools import test

inputs = [2,3,4,5,6,20,44]
outputs = [2,3,5,8,13,10946,1134903170]
funcs = [solution1]

test(inputs, outputs, funcs)