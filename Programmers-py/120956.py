'''
120956: 옹알이(1)
'''

import re

def solution(babbling):
    answer = 0
    
    target = 'aya|ye|woo|ma'
    for line in babbling:
        result = re.split(target, line)
        cnt = sum([len(r) for r in result])
        
        if cnt == 0:
            answer += 1
        
    return answer