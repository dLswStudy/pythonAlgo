from heapq import heappush
t = int(input())
tCases = []
# 케이스 별로 입력 & 힙푸시 & 정답도출
for _ in range(t):
    n = int(input())
    amountDict = {}
    maxHeap = []
    for _ in range(n):
        school, amount = input().split()
        amount = int(amount)
        heappush(maxHeap, -amount)
        amountDict[amount] = school
    maxAmt = -maxHeap[0]
    maxSchool = amountDict[maxAmt]
    tCases.append((maxAmt, maxSchool))
for tCase in tCases:
    print(tCase[1])
