MAX_VALUE = 100001
def solution(scores):
    answer = 1
    target = scores[0]
    target_sum = target[0] + target[1]

    # 점수1 별로, 점수2가 제일 높은 사람
    max_score = [0 for _ in range(MAX_VALUE+1)]
    for cur, value in scores:
        max_score[cur] = max(max_score[cur], value)
    
    # 역방향으로 점수 높은 사람 재배치
    for i in range(MAX_VALUE-1, 0, -1):
        max_score[i] = max(max_score[i], max_score[i+1])
    
    # 타켓과 비교
    for s in scores:
        if (target[0] < s[0]) and (target[1] < s[1]):
            return -1
        
        if s[1] < max_score[s[0]+1]:
            continue
        
        if target_sum < s[0] + s[1]:
            answer += 1
        
    return answer