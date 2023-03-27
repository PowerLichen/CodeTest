def solution(board):
    height = len(board)
    width = len(board[0])
    
    queue = list()
    end = None
    
    for r in range(height):
        start_pos = board[r].find('R')
        if start_pos != -1:
            queue.append((r, start_pos, 0))
        end_pos = board[r].find('G')
        if end_pos != -1:
            end = (r, end_pos)
            
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    visited = set()    
    while queue:
        cur_r, cur_c, value = queue.pop(0)
        
        if (cur_r == end[0]) and (cur_c == end[1]):
            return value
        
        value += 1
        for n in range(4):
            nxt_r = cur_r
            nxt_c = cur_c
            while True:
                if nxt_r < 0 or nxt_r >= height or nxt_c < 0 or nxt_c >= width:
                    break
                if board[nxt_r][nxt_c] == 'D':
                    break
                nxt_r += dr[n]
                nxt_c += dc[n]
            
            nxt_r -= dr[n]
            nxt_c -= dc[n]
            
            if (nxt_r, nxt_c) in visited:
                continue
            if (nxt_r == cur_r) and (nxt_c == cur_c):
                continue
            
            visited.add((nxt_r, nxt_c))
            queue.append((nxt_r, nxt_c, value))
            

    return -1
