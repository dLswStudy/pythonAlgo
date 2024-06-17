from collections import deque

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

# 그래프 만들기 [[], [2,3], [7,8,9]...]
graph = [[] for _ in range(n+1)] # 정점 0 버림
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)
print("graph = ", graph)

result = -1
visited = [False]*(n+1)
queue = deque([(a,0)])

while queue:
    current, dist = queue.popleft()
    if current == b:
        result = dist
        break
    if visited[current]:
        continue

    visited[current] = True

    for edge in graph[current]:
        if not visited[edge]:
            queue.append((edge,dist+1))

print(result)