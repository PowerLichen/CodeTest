"""
풀이:
최소 비용만 저장하는 것이 아닌, 방향별 최소비용을 저장.
"""

def solution(board):
    n = len(board)

    visited_board = [[[None]*n for _ in range(n)] for __ in range(4)]

    for i in range(4):
        visited_board[i][0][0] = 0
        visited_board[i][0][1] = 100
        visited_board[i][1][0] = 100

    moveset = ((0, -1), (0, 1), (-1, 0), (1, 0))

    queue = [(1, 0), (0, 1)]
    while queue:
        cur_r, cur_c = queue.pop(0)
        cur_value = board[cur_r][cur_c]

        for i in range(4):
            nxt_r = cur_r + moveset[i][0]
            nxt_c = cur_c + moveset[i][1]
            if nxt_r < 0 or nxt_r >= n or nxt_c < 0 or nxt_c >= n:
                continue
            if board[nxt_r][nxt_c] == 1:
                continue
            
            prev_r, prev_c = visited_board[i][cur_r][cur_c]

            nxt_value = cur_value + 100
            is_corner = (nxt_r - prev_r) & (nxt_c - prev_c)
            if is_corner != 0:
                nxt_value += 500


            
            for pos in visited_board[cur_r][cur_c]:
                prev_r, prev_c = pos
                nxt_value = cur_value + 100
                is_corner = (nxt_r - prev_r) & (nxt_c - prev_c)

                

                if (visited_board[nxt_r][nxt_c] == None):
                    visited_board[nxt_r][nxt_c] = {(cur_r, cur_c)}      
                    board[nxt_r][nxt_c] = nxt_value             
                elif (board[nxt_r][nxt_c] > nxt_value):
                    visited_board[nxt_r][nxt_c] = {(cur_r, cur_c)}
                    board[nxt_r][nxt_c] = nxt_value
                elif (board[nxt_r][nxt_c] == nxt_value):
                    visited_board[nxt_r][nxt_c].add((cur_r, cur_c))
                else:
                    continue
                    
                
                if (nxt_r, nxt_c) not in queue:
                    queue.append((nxt_r, nxt_c))

    return board[n-1][n-1]

a = 		[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
solution(a)
