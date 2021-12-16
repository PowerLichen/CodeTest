# 1238: 파티
# 다익스트라 알고리즘을 방향이 서로 다른 dict()을 사용하여 풀이.

import sys
MAX = sys.maxsize


def dijkstra(city_map, N, start):
    dist = [0] + [MAX] * (N)
    dist[start] = 0
    queue = list()
    queue.append((start, 0))

    while queue:
        cur_p, cur_cost = queue.pop(0)
        if dist[cur_p] < cur_cost:
            continue
        for next_p, next_cost in city_map[cur_p]:
            total = cur_cost+next_cost
            if dist[next_p] > total:
                dist[next_p] = total
                queue.append((next_p, total))

    return dist


# N = 학생 수, M = 도로 갯수, X = 파티 장소
N, M, X = map(int, sys.stdin.readline().split())

city_map = dict()
city_map_reverse = dict()

for i in range(1, N+1):
    city_map[i] = list()
    city_map_reverse[i] = list()

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    city_map[start].append((end, cost))
    city_map_reverse[end].append((start, cost))

print(max([a+b for a, b in zip(dijkstra(city_map, N, X),
      dijkstra(city_map_reverse, N, X))]))
