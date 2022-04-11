#2638: 치즈
# 외부공기와 내부 공기를 분리해야 하므로, BFS로 외부 공기 설정을 해준다.
# 이후 치즈 녹이기를 진행하여 풀이. 

# 외부 공기를 8로 설정
def bfs(cheese, n, m):
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    visit = [[0]*m for _ in range(n)]
    q = [(0, 0)]

    while q:
        cur_r, cur_c = q.pop(0)
        visit[cur_r][cur_c] = 1
        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == 0 and cheese[nr][nc] != 1:
                cheese[nr][nc] = 8
                visit[nr][nc] = 1
                q.append((nr, nc))


def melt_check(cheese, r, c, n, m):
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    air_cnt = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if cheese[nr][nc] == 8:
                air_cnt += 1
        if air_cnt > 1:
            return True
    return False


result = 0
n, m = map(int, input().split())
cheese = [list(map(int, input().rstrip().split())) for _ in range(n)]

while True:
    flag = False
    bfs(cheese, n, m)

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                flag = True
                if melt_check(cheese, i, j, n, m) == True:
                    cheese[i][j] = 0

    if flag == False:
        break

    result += 1

print(result)
