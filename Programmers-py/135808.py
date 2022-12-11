'''
135808: 과일 장수
'''

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score)-m+1, m):
        num = i + m - 1
        answer += score[num] * m
    return answer