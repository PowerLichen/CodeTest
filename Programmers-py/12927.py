import heapq

def solution(n, works):
    work_heap = list()
    for value in works:
        heapq.heappush(work_heap, -value)
    
    for _ in range(n):
        cur = heapq.heappop(work_heap)
        if cur == 0:
            return 0
        heapq.heappush(work_heap, cur+1)
    
    answer = 0
    for num in work_heap:
        answer += num**2
    
    return answer