# 1753: 최단경로
# 다익스트라 알고리즘을 이용하여 풀이

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = dict()

for i in range(1, V+1):
    graph[i] = dict()

for _ in range(E):
    u, v, e = map(int, sys.stdin.readline().split())
    if graph[u].get(v):
        e = min(e, graph[u][v])
    graph[u][v] = e


def dijkstra(start):
    dist = [sys.maxsize for _ in range(V+1)]
    dist[start] = 0
    q = list()
    heapq.heappush(q, (0, start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_cost:
            continue
        for next_node, next_cost in graph[cur_node].items():
            next_dist = cur_cost+next_cost
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))

    return dist


result = dijkstra(start)

for i in range(1, V+1):
    if result[i] == sys.maxsize:
        print('INF')
    else:
        print(result[i])
