#1697: 숨바꼭질
#풀이법: bfs를 이용하여 세 가지 이동방법에 대해서 결과를 체크하고 큐에 다시 집어넣는 코드를 작성.
#DP를 사용하여 이전에 방문한 위치는 더 이상 계산하지 않도록 작성.

def bfs(start, end):
    if(start == end):
        return 0

    times = [-1 for i in range(100001)]
    queue = [start]
    times[start] = 0

    while(len(queue) != 0):
        current = queue.pop(0)
        cnt = times[current]+1

        for next in [current-1, current+1, current*2]:
            if 0 <= next <= 100000 and times[next] < 0:
                if next == end:
                    return cnt
                times[next] = cnt
                queue.append(next)


n, k = map(int, input().split())
print(bfs(n, k))
