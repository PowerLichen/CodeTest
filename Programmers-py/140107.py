'''
140107: 점 찍기
원점(0, 0)으로부터 x축 방향으로 a*k(a = 0, 1, 2, 3 ...), y축 방향으로 b*k(b = 0, 1, 2, 3 ...)만큼 떨어진 위치에 점을 찍습니다.
원점과 거리가 d를 넘는 위치에는 점을 찍지 않습니다.

점이 총 몇 개 찍히는지 return.

피드백>>
x,y축이 전부 k배 좌표를 나타내기 때문에.
길이가 d/k인 원 방정식의 1사분면에 존재하는 정수 좌표점을 찾는 것과 같음.
피타고라스 정리 사용에서 대각선 길이를 미리 선언하는 것으로 변경(효율성)
'''

from math import sqrt, trunc

def solution(k, d):
    answer = 0
    d = d/k
    d_sq = d**2
    for n in range(0,trunc(d)+1):
        diff = d_sq - n**2
        max_pos = trunc(sqrt(diff))
        answer += max_pos + 1
        
    return answer


solution(2,4)