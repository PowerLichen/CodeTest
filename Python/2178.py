# 2178: 미로탐색
# BFS로 미로 탐색
from sys import stdin

n, m = map(int, stdin.readline().split())

maze_map = list()

for _ in range(n):
    maze_map.append(stdin.readline())

clear_map = [[-1]*m for _ in range(n)]

# 미로 찾기 시작
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

queue = list()
queue.append((0, 0))
clear_map[0][0] = 1

while queue:
    x, y = queue.pop(0)
    value = clear_map[x][y]
    value += 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze_map[nx][ny] == "0":
            continue
        if clear_map[nx][ny] == -1 or clear_map[nx][ny] > value:
            clear_map[nx][ny] = value
            queue.append((nx, ny))


print(clear_map[n-1][m-1])
