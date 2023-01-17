from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    jobs.sort()
    n = len(jobs)
    cur_jobs = list()
    idx = 0
    time = 0
    while True:
        while idx < n:
            if jobs[idx][0] > time:
                break
            j_time, j_value = jobs[idx]
            heappush(cur_jobs, [j_value+time-j_time, j_time, j_value])
            idx += 1
        # 레디 큐에 작업이 있을 때
        if cur_jobs:
            nxt_job = heappop(cur_jobs)
            time += nxt_job[2]
            answer += time - nxt_job[1]
        # 레디 큐에 작업이 없을 때: 디스크 대기 후 작업
        elif idx < n:
            nxt_job = jobs[idx]
            time = nxt_job[0] + nxt_job[1]
            answer += nxt_job[1] 
        # 모든 작업이 끝났을 때
        else:
            break
        
        
    return answer // n


