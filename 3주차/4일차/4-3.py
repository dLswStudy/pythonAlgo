# import sys
# input = sys.stdin.readline
# N = int(input())
# nums = list(map(int, input().split()))
#
# # dp 1  1  2  2  3  4  1  1  5
# # ex 20 13 21 15 17 23 8  5  25
# dp = [1] * N
# for i in range(N):
#     for j in range(i):
#         if nums[i] < nums[j]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

N = int(input())
nums = list(map(int, input().split()))
nums = nums[::-1]
dp = [0] * 1001
for num in nums:
    dp[num] = max(dp[:num])+1
print(max(dp))