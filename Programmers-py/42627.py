from heapq import heappush, heappop, heapify

def solution(jobs):
    heapify(jobs)
    n = len(jobs)
    job_queue = list()
    time = 0
    answer = 0
    while jobs or job_queue:
        while jobs and jobs[0][0] <= time:
            job = heappop(jobs)
            heappush(job_queue, (job[1], job[0]))
        
        if job_queue:
           c_value, c_time = heappop(job_queue)
        elif jobs:
            c_time, c_value = heappop(jobs)
            time = c_time
        time += c_value
        answer += time-c_time     
        
    return answer // n