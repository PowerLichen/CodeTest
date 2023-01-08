"""
43105: 정수 삼각형
풀이:
아래에서 역순으로 올라오면서, 각 위치에서 최선의 선택을 저장.(DP)
"""
def solution(triangle):
    depth = len(triangle) - 2

    for n in range(depth, -1, -1):
        cur_floor = triangle[n]
        for i in range(len(cur_floor)):
            cur_floor[i] += max(triangle[n+1][i], triangle[n+1][i+1])
    
    return triangle[0][0]