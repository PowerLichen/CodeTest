# 2252: 줄 세우기
# 위상정렬을 이용해 풀이
from collections import defaultdict

n,m = map(int, input().split())

order_map = defaultdict(list)
counts = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    order_map[a].append(b)
    counts[b] += 1

# 위상 정렬
q = list()
for i in range(1,n+1):
    if counts[i] == 0:
        q.append(i)


while q:
    cur = q.pop(0)
    print(cur, end = ' ')
    for num in order_map[cur]:
        counts[num] -= 1
        if counts[num] == 0:
            q.append(num)


