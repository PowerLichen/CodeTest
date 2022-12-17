'''
92334: 신고 결과 받기
'''

def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    user_lst = {id_list[i]: i for i in range(len(id_list))}
    log = {id: set() for id in id_list}
    
    for r in report:
        user, target = r.split()
        log[target].add(user)
    
    for id in id_list:
        if len(log[id]) < k:
            continue
        for r in log[id]:
            answer[user_lst[r]] += 1
        
    
    return answer