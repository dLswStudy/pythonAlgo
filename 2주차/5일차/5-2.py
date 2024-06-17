import sys
input = sys.stdin.readline
from collections import deque

n, m, r = map(int, input().split())

# 그래프 만들기 [[], [2,4], [3,4] ...]
graph = [[] for _ in range(n+1)] # 정점 0 버림
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for edges in graph:
    edges.sort()
print(graph)

# 방문여부, 방문순서, 방문순서카운트
visit = {
    'done': [False]*(n+1),
    'order': [0]*(n+1),
    'order_cnt': 0,
}

# BFS-큐 프로세스
queue = deque([r])
while queue:
    current = queue.popleft()
    # 방문한 정점이면 Pass
    if visit['done'][current]:
        continue

    # 방문 순서 저장
    visit['done'][current] = True
    visit['order_cnt'] += 1
    visit['order'][current] = visit['order_cnt']

    # 방문 안한 간선들 인큐
    for edge in graph[current]:
        if not visit['done'][edge]:
            queue.append(edge)

for order in visit['order'][1:]:
    print(order)