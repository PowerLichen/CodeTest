def solution(routes):    
    routes.sort(key=lambda x: (x[1],x[0]))
    
    r_size = len(routes)
    idx = 0
    answer = 0
    while idx < r_size:
        camera = routes[idx][1]
        answer += 1
        idx += 1
        while idx < r_size:
            if routes[idx][0] > camera:
                break
            idx += 1
    
    return answer