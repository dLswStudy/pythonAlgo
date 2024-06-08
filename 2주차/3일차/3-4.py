# 절단기 설정 높이 h 구하기
# 가장높은나무높이 maxtreeH
# 모든 나무 높이 합 sum
# 나무의 수 n, 가져가려고 하는 나무의 길이 m
# 이분탐색 / sum : min(h=maxtreeH-1) ~ mid(h=(maxtreeH-1)/2) ~ max(h=0)
# target: sum -> m
# 0 <= h < maxtreeH-1
n, m = map(int, input().split())
heights = list(map(int, input().split()))
# (h, gap)
ans = []
def calcTakeM(cutH):
    sum = 0
    global heights
    for treeH in heights:
        h = treeH - cutH
        if h >= 0:
            sum += h
    return sum

left, right = 0, max(heights) - 1
while left <= right:
    mid = (left + right) // 2
    print('left, mid, right', left, mid, right)
    calcM = calcTakeM(mid)
    if calcM >= m and m-n <= calcM <= m+n:
        ans.append(mid)
    print("calcM = ", calcM)

    if calcM == m:
        break
    elif calcM > m:
        left = mid + 1
    else:
        right = mid - 1
print(ans[-1])

