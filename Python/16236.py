# 16236: 아기 상어

size = int(input())
fish_map = list()
shark_size = 2


def find_next(start):
    global fish_map

    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]
    eatable = list()
    move_count = -1

    q = list()
    q.append((0, start))

    visit = [[False]*size for i in range(size)]

    while len(q) > 0:
        cnt, cur_p = q.pop(0)
        if move_count == cnt:
            break
        cnt += 1
        for i in range(4):
            nx, ny = cur_p[0]+move_x[i], cur_p[1]+move_y[i]
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if visit[nx][ny] or fish_map[nx][ny] > shark_size:
                continue
            if 0 < fish_map[nx][ny] < shark_size:
                eatable.append((nx, ny))
                move_count = cnt
            visit[nx][ny] = True
            q.append((cnt, (nx, ny)))

    # 먹을 물고기 선택
    result = 0
    if len(eatable) > 0:
        eatable.sort()
        start[0], start[1] = eatable[0][0], eatable[0][1]
        fish_map[start[0]][start[1]] = 0
        result = move_count

    return result


cur = [-1, -1]

find_check = True

# 맵 세팅, 아기상어 위치 찾기
for i in range(size):
    temp = list(map(int, input().split()))
    fish_map.append(temp)
    if find_check:
        for j in range(size):
            if fish_map[i][j] == 9:
                cur[0], cur[1] = i, j
                fish_map[i][j] = 0
                find_check = False

# 먹이 찾기
result = 0

req_fish = shark_size

while True:
    n = find_next(cur)
    if n == 0:
        break
    result += n
    req_fish -= 1

    # 물고기 진화 체크
    if req_fish == 0:
        shark_size += 1
        req_fish = shark_size


print(result)
