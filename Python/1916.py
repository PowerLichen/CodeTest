# 1916: 최소비용 구하기
# 다익스트라 알고리즘을 사용하여 문제를 해결. MAX value는 시스템에서 제공하는 것을 쓰자.
import sys
MAX = sys.maxsize


def dijkstra(city_map, dist, start):
    dist[start] = 0
    q = list()
    q.append((start, 0))

    while len(q) != 0:
        cur, cur_cost = q.pop(0)

        if dist[cur] < cur_cost:
            continue
        for city, next_cost in city_map[cur]:
            total_cost = cur_cost + next_cost
            if dist[city] > total_cost:
                dist[city] = total_cost
                q.append((city, total_cost))


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

city_map = dict()
dist = [MAX]*(n+1)

for i in range(1, n+1):
    city_map[i] = list()

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    city_map[start].append((end, cost))

src, dest = map(int, sys.stdin.readline().split())

dijkstra(city_map, dist, src)

print(dist[dest])
