"""
43993: 스킬트리
풀이:
선행스킬 정보를 딕셔너리로 저장하고,
각 스킬트리에 대해 선행정보와 이미 배운 스킬인가를 체크. 
"""

def check_tree(stree, pre_skill):
    learn_set = set()
    for skill in stree:
        if (skill in pre_skill) and (pre_skill[skill] not in learn_set):
            return 0
        
        learn_set.add(skill)
    
    return 1
        

def solution(skill, skill_trees):    
    pre_skill = dict()
    for i in range(1,len(skill)):
        pre_skill[skill[i]] = skill[i-1]
        
    answer = 0
    for stree in skill_trees:
        answer += check_tree(stree, pre_skill)
    
    return answer
