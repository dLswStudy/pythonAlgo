# 입력 -----------------------------------------------
from collections import deque

t = int(input())
tests = []
for _ in range(t):
    l = int(input())
    fromN, fromM = map(int, input().split())
    toN, toM = map(int, input().split())
    tests.append((l, (fromN, fromM), (toN, toM)))

# 풀이 -----------------------------------------------
# board ↓n ->m
# 1시 방향 , 2시 방향 ~ 11시 방향 (시계 방향)
dNMs = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
cheatKey = [(1,2),(2,1),(1,1),(0,2),(2,0),(0,3),(3,0)]
cheatVal = [ 1   , 1   , 2   , 2   , 2   , 3   , 3   ]

def minMove(test):
    l, fromNM, toNM = test
    tn, tm = toNM
    global dNM
    global cheatKey
    global cheatVal

    visited = [[False]*l for _ in range(l)]
    cnts = []
    cnt = 0

    queue = deque([(fromNM, cnt)])
    while queue:
        current, cnt = queue.popleft()

        # 방문 처리
        n, m = current # 현재 위치
        if visited[n][m]:
            continue
        visited[n][m] = True

        # 8개 방향 -> next 와 end 사이 거리 추정치 roughDist(distN+distM) 계산
        _8ways = []
        for dNM in dNMs:
            dn, dm = dNM
            nextN, nextM = n+dn, m+dm
            if nextN < 0 or nextM < 0:
                continue
            distN, distM = abs(tn-nextN), abs(tm-nextM)
            roughDist = distN+distM
            way = (roughDist, (distN, distM), (nextN, nextM))
            _8ways.append(way)
        _8ways.sort(key=lambda x:(x[0]))
        a, b = _8ways[:2]
        #   roughDist > 3 => 1~2개 고르기 [기준: roughDist 적은 것 , set(distN & distM 조합) 순] -> 인큐
        if a[0] > 3:
            nn,nm = a[2]
            if not visited[nn][nm]:
                queue.append((a[2], cnt+1))
            if a[0] == b[0] and a[1] != b[1]:
                nn,nm = b[2]
                if not visited[nn][nm]:
                    queue.append((b[2], cnt+1))
        #   roughDist<= 3 => distN & distM 조합 -> cheatKey 서치 -> cheatVal 이 적은 것 cnt 에 더하고 cnts 에 리스트업
        elif a[0] <= 3:
            if b[0] <= 3:
                severalCntUp = min(cheatVal[cheatKey.index(a[1])], cheatVal[cheatKey.index(b[1])])
                cnt += severalCntUp
            else:
                severalCntUp = cheatVal[cheatKey.index(a[1])]
                cnt += severalCntUp
            cnts.append(cnt)


    return min(cnts)
# 출력 -----------------------------------------------
for test in tests:
    print(minMove(test))