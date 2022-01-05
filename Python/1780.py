# 1780: 종이의 개수
# 풀이: 분할정복을 이용:

from sys import stdin

n = int(stdin.readline())
square = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = [0, 0, 0, 0]

# 분할계산
# -1 = idx0, 0 = idx1, 1 = idx0, 2 = 분해됨
def dac(data, size, x, y):
    global result
    if size == 1:
        return data[x][y]

    counts = [0, 0, 0, 0]
    div = size//3
    for i in range(x, x+size, div):
        for j in range(y, y+size, div):
            ans = dac(data, div, i, j)
            counts[ans+1] += 1
    
    # 9칸이 전부 같은 경우
    if 9 in counts:
        return counts.index(9)-1

    # 9칸이 같지 않은 경우
    for i in range(3):
        result[i] += counts[i]
    return 2


# 분할
result[dac(square, n, 0, 0)+1] += 1

for i in range(3):
    print(result[i])