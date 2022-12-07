'''
120924: 다음에 올 숫자
'''

def solution(common):    
    diff = common[1] - common[0]
    
    if common[2] - common[1] == diff:
        return common[-1] + diff
    
    return common[-1] * (common[1]/common[0])