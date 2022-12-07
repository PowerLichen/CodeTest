'''
87377: 교점에 별 만들기
'''

import itertools


def check_cross(l1, l2):
    a1,b1,c1 = l1
    a2,b2,c2 = l2
    
    if a1*b2 == a2*b1:
        return None
    
    x = (b1*c2 - b2*c1) / (a1*b2 - a2*b1)
    if int(x) != x:
        return None
    
    y = (a2*c1 - a1*c2) / (a1*b2 - a2*b1)
    if int(y) != y:
        return None
    
    return (int(x), int(y))
    
    

def solution(line):
    cross = set()
    
    for l1,l2 in list(itertools.combinations(line,2)):
        result = check_cross(l1,l2)
        if result == None:
            continue
        cross.add(result)
            
    cross = list(cross)
    
    xs, ys = zip(*cross)
    pos_min, pos_max = (min(xs), min(ys)), (max(xs), max(ys))
    
    size_w, size_h = pos_max[0] - pos_min[0], pos_max[1] - pos_min[1]
    
    answer = [['.'for _ in range(size_w+1)] for __ in range(size_h+1)]

    for x,y in cross:
        rel_x, rel_y = x - pos_min[0], size_h - (y - pos_min[1])
        answer[rel_y][rel_x] = '*'
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer