'''
118666: 성격 유형 검사하기
'''

def solution(survey, choices):
    answer = ''
    types = ['R','T', 'C','F','J','M','A','N']
    scores = {ch:0 for ch in types}
    for ids, n in zip(survey, choices):
        if n < 4:
            scores[ids[0]] += 4 - n
        elif n > 4:
            scores[ids[1]] += n - 4
    
    for n in range(0,8,2):
        t1,t2 = types[n], types[n+1]
        if scores[t1] >= scores[t2]:
            answer += t1
        if scores[t1] < scores[t2]:
            answer += t2
            
            
    return answer