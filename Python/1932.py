#1932: 정수 삼각형
n = int(input())
before = [0]

for i in range(n):
    cur = list(map(int,input().split()))
    
    cur[0] += before[0]
    for j in range(1, i):
        cur[j] += max(before[j-1],before[j])
    cur[-1] += before[-1]

    before = cur


print(max(cur))