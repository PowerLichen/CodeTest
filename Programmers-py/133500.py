from collections import defaultdict

def solution(n, lighthouse):
    light_graph = defaultdict(list)
    for lh_a, lh_b in lighthouse:
        light_graph[lh_a].append(lh_b)
        light_graph[lh_b].append(lh_a)
    
    # check leaf node
    answer = 0
    cur = 1
    visit_check = [False for _ in range(n+1)]
    light_set = set()
    for i in range(1,n+1):
        if len(light_graph[i]) > 1:
            continue
        
        visit_check[i] = True
        
        light_idx = light_graph[i][0]
        if light_idx in light_set:
            continue
        
        cur = light_idx
        light_set.add(light_idx)
    
    answer += len(light_set)
    
    # bfs
    stack = [(cur, 0)]
    while stack:
        nxt, weight = stack.pop()
        visit_check[nxt] = True

        if nxt in light_set:
            if weight > 2:
                answer += 1
            weight = 0
        
        for node in light_graph[nxt]:                
            if visit_check[node] == True:
                continue                
            stack.append((node, weight+1))
        
    
        
    return answer