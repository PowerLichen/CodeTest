# 2623: 음악 프로그램
# 위상정렬을 이용한 문제 풀이. 보조 PD들의 중복 체크 필수.
#  메인 PD가 순서를 못 정하는 경우도 생각해야 하므로 결과를 바로 출력하지 않고, result에 저장 후 출력하도록 구현

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = list()
order_map = defaultdict(list)
counts = [0] * (n+1)

for _ in range(m):
    pd = list(map(int, input().split()))
    for i in range(2, pd[0]+1):
        before_n, next_n = pd[i-1],pd[i]
        if next_n in order_map[before_n]:
            continue
        order_map[before_n].append(next_n)
        counts[next_n] += 1

#위상 정렬
q = deque()
for i in range(1,n+1):
    if counts[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    result.append(cur)
    for num in order_map[cur]:
        counts[num] -= 1
        if counts[num] == 0:
            q.append(num)


if len(result) == n:
    print(*result, sep= '\n')
else:
    print(0)