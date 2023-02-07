def solution(n, times):
    answer = 0
    time_left = 0
    time_right = max(times) * n
    while time_left <= time_right:
        cur_time = (time_left + time_right) // 2

        count_people = 0
        for time in times:
            count_people += cur_time // time

        if count_people >= n:
            time_right = cur_time - 1
            answer = cur_time
        else:
            time_left = cur_time + 1

    return answer