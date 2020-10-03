# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. 
# You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

# Note:
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].

def solution1(cost):
    if len(cost) < 2: return 0
    steps = {0: cost[0]}
    last_step = len(cost)-1
    for n in range(1, len(cost)):
        if n-2 in steps: steps[n] = min(steps[n-1],steps[n-2]) + cost[n]
        else: steps[n] = cost[n]
    return min(steps[last_step],steps[last_step-1])

def solution2(cost):
    cost.append(0)
    price_list = [0] * len(cost)
    price_list[0] = cost[0]
    price_list[1] = cost[1]
    for idx in range(2,len(cost)): price_list[idx] = min(price_list[idx-1],price_list[idx-2]) + cost[idx]
    return price_list[-1]

from tools import test
inputs = [[10,15,20],[1,100,1,1,1,100,1,1,100,1]]
outputs = [15,6]
funcs = [solution1, solution2]

test(inputs, outputs, funcs)