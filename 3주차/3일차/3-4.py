'''
1->(v1/v2)->(v2/v1)->N
 (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
'''
# n, e = 4, 6
# graph = {1: {2: 3, 3: 5, 4: 4}, 2: {1: 3, 3: 3, 4: 5}, 3: {2: 3, 4: 1, 1: 5}, 4: {3: 1, 2: 5, 1: 4}}
# v1, v2 = 2, 3

import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

n, e = map(int, input().split())
graph = defaultdict(dict)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())

def minDist(va, vb):
    minDist = {node:float('inf') for node in graph}
    minDist[va] = 0

    priority_queue = [(0, va)]
    while priority_queue:
        curr_route_dist, curr_node = heapq.heappop(priority_queue)

        if minDist[curr_node] < curr_route_dist:
            continue

        for neighbor, to_neib_dist in graph[curr_node].items():
            new_route_dist = curr_route_dist + to_neib_dist
            if minDist[neighbor] > new_route_dist:
                minDist[neighbor] = new_route_dist
                heapq.heappush(priority_queue, (new_route_dist, neighbor))

    return minDist.get(vb, -1)


toV1 = minDist(1, v1)
toV2 = minDist(1, v2)
v1ToV2 = minDist(v1, v2)
v1ToN = minDist(v1, n)
v2ToN = minDist(v2, n)

route1 = [toV1, v1ToV2, v2ToN]
route2 = [toV2, v1ToV2, v1ToN]
if -1 in route1 or -1 in route2:
    print(-1)
else:
    print(min(sum(route1), sum(route2)))


