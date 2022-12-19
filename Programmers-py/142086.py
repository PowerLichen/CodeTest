'''
142086: 가장 가까운 같은 글자
'''

def solution(s):
    alpha_p = dict()
    
    answer = [0] * len(s)
    
    for i in range(len(s)):
        ch = s[i]
        pos = alpha_p.get(ch)
        answer[i] = -1 if pos == None else (i - pos)
        alpha_p[ch] = i
        
    return answer

