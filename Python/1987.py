# 1987: 알파벳
# 재귀 DFS로 경로를 찾는 완전탐색을 사용. pypy로 제출.

r, c = map(int, input().split())
maze = [list(map(lambda a: ord(a)-65, input())) for _ in range(r)]

al_check = [False for _ in range(26)]
answer = 0
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs_rec(cur_r, cur_c, visit_cnt):
    global answer
    if answer < visit_cnt:
        answer = visit_cnt
    
    al_check[maze[cur_r][cur_c]] = True

    for i in range(4):
        nr, nc = cur_r+dr[i], cur_c+dc[i]
        if 0 <= nr < r and 0 <= nc < c and al_check[maze[nr][nc]] == False:
            dfs_rec(nr, nc, visit_cnt+1)

    al_check[maze[cur_r][cur_c]] = False


dfs_rec(0, 0, 1)
print(answer)
