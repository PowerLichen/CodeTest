# 14870: 조개 줍기
import sys

N = int(sys.stdin.readline())
dp = [[0]*(N+1) for _ in range(N+1)]
result = 0

for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N+1):
        dp[i][j] = temp[j-1]

# 최대값 계산
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + dp[i][j]
        result += dp[i][j]

print(result)


# 쿼리 계산
for _ in range(N):
    op, i, j = sys.stdin.readline().split()
    value = 1
    if op == "D":
        value = -1
    count = 0
    queue = [(int(i), int(j))]

    while queue:
        x, y = queue.pop(0)
        dp[x][y] += value
        count += 1

        # 아래 체크
        if x < N:
            nx, ny = x+1, y
            if dp[x][y] > dp[nx][ny-1]:
                queue.append((nx, ny))
        # 오른쪽 체크
        if y < N:
            nx, ny = x, y+1
            if dp[x][y] > dp[nx-1][ny]:
                queue.append((nx, ny))

    result += value*count
    print(result)