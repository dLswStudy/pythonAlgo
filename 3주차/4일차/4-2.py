from collections import defaultdict
import sys
input = sys.stdin.readline
T = int(input())
testCases = [(int(input()),int(input())) for _ in range(T)]

# dp
# \   0       1       2       3       4       5
# 0   0ho x   1       2       3       4       5
# 1           1       3       6       10      15
# 2           1       4       10      20
# 3
# 4

memo = defaultdict(lambda: defaultdict(int))
def dp(a, b):
    if memo[a][b]:
        return memo[a][b]
    else:
        if b == 0:
            return 0
        elif a == 0:
            memo[a][b] = b
            return b
        else:
            memo[a][b] = dp(a, b-1) + dp(a-1, b)
            return dp(a, b-1) + dp(a-1, b)

for tc in testCases:
    print(dp(*tc))