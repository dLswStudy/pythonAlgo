import heapq

def dijkstra(graph, start):
    min_dist = {node: float('inf') for node in graph}
    min_dist[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        curr_route_dist, curr_node = heapq.heappop(priority_queue)

        if curr_route_dist > min_dist[curr_node]:
            continue

        for neighbor, to_neighbor_dist in graph[curr_node].items():
            calc_dist = curr_route_dist + to_neighbor_dist

            if calc_dist < min_dist[neighbor]:
                min_dist[neighbor] = calc_dist
                heapq.heappush(priority_queue, (calc_dist, neighbor))

    return min_dist

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print(f"{start_node}로부터 다른 모든 정점까지의 최단 경로:", dijkstra(graph, start_node))