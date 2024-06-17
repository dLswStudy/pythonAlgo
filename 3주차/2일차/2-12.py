'''
N×N인 격자,  검은색 블록, 무지개 블록, 일반 블록
일반 블록은 M가지 색상,  색은 M이하의 자연수
검은색 블록은 -1, 무지개 블록은 0
블록 그룹,  그룹에는 일반 블록이 적어도 하나,  일반 블록의 색은 모두 같아야 한다
    검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
    그룹에 속한 블록의 개수는 2보다 크거나 같아야 함.
    임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
    기준블록: 행,열 순 작은 일반블록

오토플레이 기능 (블록그룹 존재하는 동안)
    크기가 가장 큰 블록 그룹을 찾는다. (무지개 블록의 수 ↑,기준블록의 행 ↑, 열 ↑ 순)
    -> 모든 블록 제거, 블록수 B, B^2 획득
    -> 격자에 중력이 작용한다.
    -> 격자가 90도 반시계 방향으로 회전한다.
    -> 다시 격자에 중력이 작용한다.
    -> 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
    ->
'''
import time



from collections import deque

# n, color = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# # n, color = 6, 4
# # board = [[2, 3, 1, 0, -1, 2], [2, -1, 4, 1, 3, 3], [3, 0, 4, 2, 2, 1], [-1, 4, -1, 2, 3, 4], [3, -1, 4, 2, 0, 3], [1, 2, 2, 2, 2, 1]]
n, color = 5, 3
board = [[2, 2, -1, 3, 1], [3, 3, 2, 0, -1], [0, 0, 0, 1, 2], [-1, 3, 1, 3, 2], [0, 3, 2, 2, 1]]

visited = [[False] * n for _ in range(n)]
max_groupInfo = (0,0,0,0,[])
_sum = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def spread_add(i, j):
    start_time = time.perf_counter()
    rainbowCnt = 0
    now_group = []
    rainbows = []
    group_color = board[i][j]
    queue = deque()
    now_group.append((i, j))
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] <= -1 or visited[nx][ny]:
                continue

            next = board[nx][ny]
            if next == group_color or next == 0:
                visited[nx][ny] = True
                now_group.append((nx, ny))
                queue.append((nx, ny))

            if next == 0: # 무지개블록
                rainbows.append((nx,ny))
                rainbowCnt += 1

    # 무지개블록은 방문 다시 해제
    for x,y in rainbows:
        visited[x][y] = False

    return (rainbowCnt, now_group)

    end_time = time.perf_counter()
    print(f"spread_add time : {end_time - start_time}s")

def calc_max_group():
    start_time = time.perf_counter()
    global _sum
    global max_groupInfo
    print("max_group = ", max_groupInfo)
    print("len(max_group) = ", max_groupInfo[0])
    _sum += max_groupInfo[0] ** 2
    print("_sum = ", _sum)
    for x, y in max_groupInfo[4]:
        board[x][y] = -9
    print("calc_max_group -> board = ")
    end_time = time.perf_counter()
    print(f"calc_max_group time : {int((end_time - start_time) * 1000)}ms")
    printBoard()


def clear():
    global visited
    global max_groupInfo
    max_groupInfo = (0,0,0,0,[])
    visited = [[False] * n for _ in range(n)]


def gravity():
    start_time = time.perf_counter()
    for j in range(n):
        for i in range(n - 2, -1, -1):
            if board[i][j] >= 0:
                nowX = i
                while True:
                    nextX = nowX + 1
                    if nextX <= n - 1 and board[nextX][j] == -9:
                        board[nextX][j] = board[nowX][j]
                        board[nowX][j] = -9
                        nowX = nextX
                    else:
                        break
    end_time = time.perf_counter()
    print(f"gravity time : {int((end_time - start_time) * 1000)}ms")
    print("gravity -> board = ")
    printBoard()


def rotate():
    global board
    board = list(map(list, zip(*board)))[::-1]
    print("rotate -> board = ")
    printBoard()


def printBoard():
    for row in board:
        print('  ', end='')
        print(row)
    print()


existNormal = True
while existNormal:
    start_time = time.perf_counter()
    existNormal = False
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                rainbowCnt, now_group = spread_add(i, j)
                if len(now_group) >= 2:
                    existNormal = True
                    groupInfo = (len(now_group), rainbowCnt, i, j, now_group[:])
                    nowAndMax = [groupInfo, max_groupInfo]
                    nowAndMax.sort(reverse=True)
                    max_groupInfo = nowAndMax[0]

    end_time0 = time.perf_counter()
    print(f"autoplay n회 1단계 time : {end_time0 - start_time}s")
    if not existNormal:
        break
    start_time2 = time.perf_counter()
    calc_max_group()
    end_time2 = time.perf_counter()
    print(f"autoplay n회 2단계 time : {end_time2 - start_time2}s")
    clear()
    start_time3 = time.perf_counter()
    gravity()
    end_time3 = time.perf_counter()
    print(f"autoplay n회 3단계 time : {end_time3 - start_time3}s")
    start_time4 = time.perf_counter()
    rotate()
    end_time4 = time.perf_counter()
    print(f"autoplay n회 4단계 time : {end_time4 - start_time4}s")
    gravity()
    end_time = time.perf_counter()
    print('ggg', end_time)
    print(f"autoplay n회 time : {end_time - start_time}s")
    print("autoplay n회 종료")
    print('-------')


print(_sum)
