
def solution(triangle):
    depth = len(triangle) - 2

    for n in range(depth, -1, -1):
        cur_floor = triangle[n]
        for i in range(len(cur_floor)):
            cur_floor[i] += max(triangle[n+1][i], triangle[n+1][i+1])
    
    return triangle[0][0]