from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(a, tree, parent, cur):
    result = 0
    
    for nxt in tree[cur]:
        if nxt == parent:
            continue
        result += dfs(a, tree, cur, nxt)
    
    a[parent] += a[cur]
    result += abs(a[cur])
    return result
    

def solution(a, edges):
    tree = defaultdict(list)
    for n1,n2 in edges:
        tree[n1].append(n2)
        tree[n2].append(n1)
        
    result = dfs(a,tree,0,0)

    if a[0] == 0:
        return result
    return -1


solution(	[-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])