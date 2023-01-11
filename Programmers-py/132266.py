from collections import defaultdict

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    map_cost = [-1 for _ in range(n+1)]
    map_cost[destination] = 0
    q = [destination]
    while q:
        cur = q.pop(0)
        nxt_cost = map_cost[cur] + 1

        for nxt in graph[cur]:
            if map_cost[nxt] != -1:
                continue
            q.append(nxt)
            map_cost[nxt] = nxt_cost

    
    return [map_cost[s] for s in sources]