
def time_to_num(x):
    hour, minute = map(int, x.split(':'))
    return hour*60 + minute


    
def solution(n, t, m, timetable):
    timetable.sort()
    timetable = list(map(time_to_num, timetable))

    # Start Time 09:00 = 9 * 60 = 540
    bustime_last = 540 + (n-1)*t
    idx = 0
    for time in range(540, bustime_last, t):
        for _ in range(m):
            if idx == len(timetable):
                break
            if timetable[idx] > time:
                break
            idx += 1

    last_idx = len(timetable)
    for i in range(idx, len(timetable)):
        if timetable[i] > bustime_last:
            last_idx = i
            break

    if (last_idx - idx) < m:
        result = bustime_last
    else:
        result = timetable[idx+m-1] - 1

    return f'{result//60:0>2}:{result%60:0>2}'

