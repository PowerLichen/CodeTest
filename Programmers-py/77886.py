'''
77886: 110 옮기기
110을 전부 빼고, 결과로 나온 문자열을 다시 110 빼기 수행 => 시간초과
110을 빼고 남은 값들을 스택에 저장할 때, 110이 만들어지면 바로 count를 증가시키도록 풀이.
'''

# 1: 110이 남지 않을때까지 110을 빼는 방법
# def swap(t):
#     temp = ''
#     start, cnt = 0, 0
#     while True:
#         div = t.find(TARGET_STRING, start)
#         if div < 0:
#             t = temp + t[start:]
#             if t.find(TARGET_STRING) == -1:
#                 break
#             temp = ''
#             start = 0
#             continue

#         temp += t[start:div]
#         cnt += 1
#         start = div+3

#     div = t.rfind('0') + 1

#     return t[:div] + TARGET_STRING*cnt + t[div:]

# 2: 스택을 사용한 방법.
TARGET_STRING = "110"

def append_str(s,stack):
    cnt = 0
    s = list(s)
    for ch in s:
        if stack[-2:] == ['1','1'] and ch == '0':
            stack.pop()
            stack.pop()
            cnt += 1
            continue
        stack.append(ch)

    return cnt

def stackswap(s):
    stack = list()
    start, cnt = 0,0
    while True:
        div = s.find(TARGET_STRING, start)
        if div < 0:
            cnt += append_str(s[start:], stack)
            break

        cnt += 1            
        cnt += append_str(s[start:div], stack)        
        start = div + 3

    temp = ''.join(stack)
    div = temp.rfind('0') + 1

    return temp[:div] + TARGET_STRING*cnt + temp[div:]


def solution(s):
    answer = [None] * len(s)
    for i in range(len(s)):
        answer[i] = stackswap(s[i])
    return answer
