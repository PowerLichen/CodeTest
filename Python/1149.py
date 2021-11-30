# 1149: RGB거리
# DP를 이용한 문제. 현재 집을 이전에 고른 경우의 최소값으로 계속 계산해나가면서 풀이.


n = int(input())

data = [[0]*3 for i in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    data[i][0] = r
    data[i][1] = g
    data[i][2] = b

for i in range(1,n):
    data[i][0] += min(data[i-1][1], data[i-1][2]) 
    data[i][1] += min(data[i-1][0], data[i-1][2]) 
    data[i][2] += min(data[i-1][0], data[i-1][1])

print(min(data[-1]))