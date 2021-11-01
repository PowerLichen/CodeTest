# 15654: N과 M(5)
# 풀이법: dfs를 이용하여 문제를 해결

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
check = [False for _ in range(n)]
result = []


def dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if check[i] == False:
            check[i] = True
            result.append(numlist[i])
            dfs(depth+1)
            result.pop()
            check[i] = False


numlist.sort()

dfs(0)
