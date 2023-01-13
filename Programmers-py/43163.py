def change_check(begin, target):
    count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            count += 1
            
    if count == 1:
        return True
    
    return False
        
def solution(begin, target, words):
    if target not in words:
        return 0
    
    lst_size = len(words)
    visited = [-1 for _ in range(lst_size)]
    q = [(begin, 0)]
    while q:
        cur, cost = q.pop(0)
        for i, word in enumerate(words):
            if visited[i] > 0:
                continue
            if change_check(cur, word):
                nxt_cost = cost + 1
                if word == target:
                    return nxt_cost
                visited[i] = nxt_cost
                q.append((word, nxt_cost))
            
    return 0

