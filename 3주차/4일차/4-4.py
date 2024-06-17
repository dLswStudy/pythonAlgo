T = int(input())
testCases = [int(input()) for _ in range(T)]

# i>=4 -> dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
dp = [-1,1,2,4] + [-1]*7
def dpFunc(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = dpFunc(n-1) + dpFunc(n-2) + dpFunc(n-3)
        return dp[n]

for tc in testCases:
    print(dpFunc(tc))