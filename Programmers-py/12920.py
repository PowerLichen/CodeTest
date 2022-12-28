def solution(n, cores):
    if len(cores) >= n:
        return n-1

    n -= len(cores)
    left, right = 1, max(cores)*n

    while left < right:
        mid = (left + right) // 2
        cleared = sum([mid//c for c in cores])

        if cleared < n:
            left = mid + 1
        else:
            right = mid

    last_time = right-1
    n -= sum([last_time//c for c in cores])

    for i, core in enumerate(cores):
        if right % core != 0:
            continue
        if n == 1:
            return i+1
        n -= 1

    return -1
