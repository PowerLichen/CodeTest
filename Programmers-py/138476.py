'''
138476: 귤 고르기
수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매할 때 서로 다른 종류의 수를 최소화.

한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어질 때,
귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return.

피드백 >>
defaultdict를 사용하여 선언되지 않은 딕셔너리 값은 0으로 초기화하고,
defaultdict의 values() 메소드 사용시 list가 반환되므로, 불필요한 재할당 제거
'''

from collections import defaultdict 

def solution(k, tangerine):
    answer = 0
    group_t = defaultdict(int)
    for t in tangerine:
        group_t[t] += 1
        
    counts = sorted(group_t.values(), reverse=True)
    
    for n in counts:
        answer += 1
        k -= n
        if k <= 0:
            break
    
    return answer