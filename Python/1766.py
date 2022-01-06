#1766: 문제집
#풀이: 위상정렬에 우선순위 큐를 사용하여, 현재 풀 수 있는 문제 중 가장 쉬운 것 부터 푼다.

from sys import stdin
from queue import PriorityQueue

result = list()
n, m = map(int, stdin.readline().split())
solved_check = [False] * (n+1)
linecount = [0] * (n+1)
linecount[0] = -1

testlist = dict()
for i in range(1, n+1):
    testlist[i] = list()

for _ in range(m):
    before, after = map(int, stdin.readline().split())
    testlist[before].append(after)
    linecount[after] += 1

pq = PriorityQueue()
# 차수가 0인 문제를 큐에 넣기
for i in range(1, n+1):
    if linecount[i] == 0:
        pq.put(i)

# 순환일경우 1 추가
if pq.empty():
    pq.put(1)

while not pq.empty():
    i = pq.get()
    result.append(i)
    solved_check[i] = True
    for idx in testlist[i]:
        linecount[idx] -= 1
        if linecount[idx] == 0 and not solved_check[idx]:
            pq.put(idx)


print(' '.join(map(str, result)))
