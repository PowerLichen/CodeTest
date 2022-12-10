'''
132267: 콜라 문제
'''

def solution(a, b, n):
    answer = 0
    while n // a > 0:
        recycle = n // a
        n -= recycle * a
        recycle = recycle * b
        answer += recycle
        n += recycle
        
    return answer