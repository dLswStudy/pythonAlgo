import sys
input = sys.stdin.readline

n, m, r = map(int,input().split()) # 정점의 수, 간선의 수, 시작 정점

# 그래프 만들기 (index+1:정점, 간선->내림차순 정렬)
# [[4,2], [4,3] ... ]
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v)
    graph[v-1].append(u)
for edges in graph:
    edges.sort(reverse=True)

# 방문 관련 데이터
visit = {
    'done':[False]*n,
    # 순서 list [정점1의 순서, 정점2의순서 ...]
    'order':[0]*n,
    'order_cnt': 0,
}


stack = [r]
while stack:
    current = stack.pop()
    if visit['done'][current - 1]:
        continue

    visit['done'][current - 1] = True
    visit['order_cnt'] += 1
    visit['order'][current - 1] = visit['order_cnt']

    # 방문
    for edge in graph[current-1]:
        if not visit['done'][edge - 1]:
            stack.append(edge)

# 스타트
for order in visit['order']:
    print(order)

