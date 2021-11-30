# 11725: 트리의 부모 찾기
# BFS를 활용하여 모든 노드의 자식을 체크하면서 풀이.
# sys.stdin.readline()는 input() 대신 사용되며, 빠른 입력


import sys

n = int(sys.stdin.readline())
tree_data = dict()
result = [0] * (n+1)
check = [False] * (n+1)

for i in range(1, n+1):
    tree_data[i] = list()

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree_data[a].append(b)
    tree_data[b].append(a)

q = list()
q.append(1)
check[1] = True

while len(q) != 0:
    cur = q.pop(0)
    for child in tree_data[cur]:
        if check[child] == False:
            check[child] = True
            result[child] = cur
            q.append(child)

# 결과 출력
for i in range(2,n+1):
    print(result[i])
