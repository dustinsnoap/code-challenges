# You are playing the following Nim Game with your friend: 
# There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
# The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

# Both of you are very clever and have optimal strategies for the game. 
# Write a function to determine whether you can win the game given the number of stones in the heap.

# Example:
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the game;
#              No matter 1, 2, or 3 stones you remove, the last stone will always be 
#              removed by your friend.

def canWinNim(n):
    return not n % 4 == 0

def canWinNim2(n):
    if n < 4: return True
    return not n % 4 == 0

inputs = [1,2,3,4,5,6,7,8,9,10,11,12,13]
outputs = [True,True,True,False,True,True,True,False,True,True,True,False,True]
funcs = [canWinNim, canWinNim2]

from tools import test
test(inputs, outputs, funcs)