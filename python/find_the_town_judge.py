# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

# Example 1:
# Input: N = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

# Example 4:
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1

# Example 5:
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3

# Exmaple 6:
# Input: N = 11, trust = [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]

# Exmaple 7:
# Input: N = 1, trust = []
# Output: 1

# Exmaple 8:
# Input: N = 2, trust = []
# Output: -1

# Constraints:
# 1 <= N <= 1000
# 0 <= trust.length <= 10^4
# trust[i].length == 2
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N

def findJudge(N, trust):
    if N == 1: return 1
    if len(trust[0]) == 0: return -1
    villagers = set()
    votes = {}
    for villager in trust:
        villagers.add(villager[0])
        if villager[1] not in votes: votes[villager[1]] = 1
        else: votes[villager[1]] += 1
    suspects = set([n for n in range(1,N+1)]).difference(villagers)
    for judge in suspects:
        if judge in votes and votes[judge] == N-1: return judge
    return -1

inputs = [[2,[[1,2]]],[3,[[1,3],[2,3]]],[3,[[1,3],[2,3],[3,1]]],[3,[[1,2],[2,3]]],[4,[[1,3],[1,4],[2,3],[2,4],[4,3]]]]
outputs = [2,3,-1,-1,3]
funcs = [findJudge]

print(findJudge(2,[[1,2]]))
print(findJudge(3,[[1,3],[2,3]]))
print(findJudge(3,[[1,3],[2,3],[3,1]]))
print(findJudge(3,[[1,2],[2,3]]))
print(findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(findJudge(11,[[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]))
print(findJudge(1,[[]]))
print(findJudge(2,[[]]))
