"""
87391: 공 이동 시뮬레이션
풀이:
쿼리 역순으로 이전 쿼리를 만족 시키는 범위를 순차적으로 찾기.
현 위치가 가장자리일 경우, 범위가 늘어나지만
가장자리가 아니라면 전체 범위 이동
"""
def solution(n, m, x, y, queries):
    answer = [x,y,x+1,y+1]
    
    queries.reverse()
    for query, value in queries:
        if query == 0:
            if answer[1] != 0:
                answer[1] = min(answer[1]+value, m)
            answer[3] = min(answer[3]+value, m)
        elif query == 1:
            if answer[3] != m:
                answer[3] = max(answer[3]-value, 0)
            answer[1] = max(answer[1]-value, 0)   
        elif query == 2:
            if answer[0] != 0:
                answer[0] = min(answer[0]+value, n)
            answer[2] = min(answer[2]+value, n)
        elif query == 3:
            if answer[2] != n:
                answer[2] = max(answer[2]-value, 0)
            answer[0] = max(answer[0]-value, 0)

        if answer[0] == answer[2] or answer[1] == answer[3]:
            return 0

    return (answer[3] - answer[1])*(answer[2] - answer[0])