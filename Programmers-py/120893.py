'''
120893: 대문자와 소문자
'''

def solution(my_string):
    answer = ''
    for ch in my_string:
        answer += ch.lower() if ch.isupper() else ch.upper()
    return answer