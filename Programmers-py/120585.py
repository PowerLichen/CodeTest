'''
120585: 머쓱이보다 키 큰 사람
'''

def solution(array, height):
    answer = 0
    for other in array:
        if other > height:
            answer += 1
    return answer