# 14052: 연구소
# 풀이법:

import copy

n, m = map(int, input().split())
array = [[] for _ in range(n)]
result = 0

dir_r = (0, 0, 1, -1)
dir_c = (1, -1, 0, 0)

for i in range(n):
    array[i] = list(map(int, input().split()))


# 벽 고르기
def select_wall(r, c, count):
    global result
    # 벽이 모두 골라진 경우
    if count == 3:
        temp_array = copy.deepcopy(array)
        for i in range(n):
            for j in range(m):
                if temp_array[i][j] == 2:
                    virus_check(i, j, temp_array)
        safe_area = sum([n.count(0) for n in temp_array])
        result = max(result, safe_area)
        return
    else:
        for i in range(n):
            for j in range(m):
                if array[i][j] == 0:
                    array[i][j] = 1
                    select_wall(i, j, count+1)
                    array[i][j] = 0


def virus_check(r, c, array):
    for i in range(4):
        next_r = r + dir_r[i]
        next_c = c + dir_c[i]
        if (0 <= next_r < n) and (0 <= next_c < m):
            if array[next_r][next_c] == 0:
                array[next_r][next_c] = 2
                virus_check(next_r, next_c, array)


select_wall(0, 0, 0)
print(result)
