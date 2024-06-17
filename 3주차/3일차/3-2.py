n = int(input())
hights = list(map(int, input().split()))

maxCnt = 0
cnt = 0
maxNum = hights[0]
for i in range(n):
    if maxNum > hights[i]:
        cnt += 1
    elif maxNum < hights[i]:
        maxNum = hights[i]
        maxCnt = max(maxCnt, cnt)
        cnt = 0

    maxCnt = max(cnt, maxCnt)
print(maxCnt)