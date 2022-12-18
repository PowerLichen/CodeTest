'''
131128: 숫자 짝궁
'''

def solution(X, Y):
    answer = ''
    x_dict = {str(n):0 for n in range(10)}
    y_dict = {str(n):0 for n in range(10)}
    
    for ch in X: x_dict[ch] += 1
    for ch in Y: y_dict[ch] += 1
    
    for n in range(9,-1,-1):
        ch = str(n)
        answer += ch*(min(x_dict[ch], y_dict[ch]))
    
    
    if len(answer) == 0:
        return '-1'
    if answer[0] == '0':
        return '0'
    
    return answer