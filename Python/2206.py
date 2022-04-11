# 2206: 벽 부수고 이동하기
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for __ in range(n)]


def find_path():
    q = deque()
    q.append((0, 0, 0))
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    visit[0][0][0] = 1

    while q:
        r, c, isBreak = q.popleft()
        if r == n-1 and c == m-1:
            return visit[r][c][isBreak]
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if (0 <= nr < n and 0 <= nc < m):
                if maze[nr][nc] == 0 and visit[nr][nc][isBreak] == 0:
                    q.append((nr, nc, isBreak))
                    visit[nr][nc][isBreak] = visit[r][c][isBreak]+1
                elif maze[nr][nc] == 1 and isBreak == 0:
                    q.append((nr, nc, 1))
                    visit[nr][nc][1] = visit[r][c][0]+1

    return -1


print(find_path())
