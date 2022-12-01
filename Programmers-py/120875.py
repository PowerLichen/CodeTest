'''
120875: 평행
'''

def solution(dots):
    answer = 0
    x,y = dots[0][0], dots[0][1]
    target = (None,(2,3),(1,3),(1,2))
    for i in range(1,4):
        dx1 = x - dots[i][0]
        dy1 = y - dots[i][1]
        n1,n2 = target[i]
        
        dx2 = dots[n1][0] - dots[n2][0]
        dy2 = dots[n1][1] - dots[n2][1]
        
        if dy1 * dx2 == dx1 * dy2:
            return 1

    
    return 0