def is_edge(panel, r, c):
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if panel[i][j] == 0:
                return True

    return False


def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    MAX_SIZE = 102
    panel = [[0]*MAX_SIZE for _ in range(MAX_SIZE)]

    for x1, y1, x2, y2 in rectangle:
        for i in range(y1*2, y2*2+1):
            for j in range(x1*2, x2*2+1):
                panel[i][j] = -1

    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            if panel[i][j] == 0:
                continue
            if is_edge(panel, i, j):
                panel[i][j] = -2

    panel[characterY][characterX] = 1
    stack = [(characterY, characterX)]
    moveset_r = [1, -1, 0, 0]
    moveset_c = [0, 0, 1, -1]
    answer = list()
    while stack:
        cur_r, cur_c = stack.pop()
        value = panel[cur_r][cur_c]

        if cur_r == itemY and cur_c == itemX:
            answer.append(value)
            panel[cur_r][cur_c] = -2
            continue

        for num in range(4):
            nxt_r = cur_r + moveset_r[num]
            nxt_c = cur_c + moveset_c[num]

            if panel[nxt_r][nxt_c] == -2:
                stack.append((nxt_r, nxt_c))
                panel[nxt_r][nxt_c] = value + 1

    return min(answer) // 2