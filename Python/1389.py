# 1389: 케빈 베이컨의 6단계 법칙
# 풀이: 그래프 정보를 딕셔너리로 저장하고, 너비 우선 탐색으로 각 점에 대한 최단거리를 계산한다.
# 계산한 최단거리를 모두 합산하여 케빈 베이컨 수를 얻어, 최소값과 비교한다.


n, m = map(int, input().split())

friendships = dict()

min_idx, min_value = 0, float('inf')

for i in range(1, n+1):
    friendships[i] = list()

for i in range(m):
    a, b = map(int, input().split())
    friendships[a].append(b)
    friendships[b].append(a)


for i in range(1, n+1):
    result_nums = [-1] * (n+1)
    result_nums[i] = 0
    queue = list()
    queue.append((i, 0))

    while queue:
        cur, dist = queue.pop(0)
        dist += 1
        for next in friendships[cur]:
            if result_nums[next] < 0:
                result_nums[next] = dist
                queue.append((next, dist))

    result = sum(result_nums) + 1
    if result < min_value:
        min_value = result
        min_idx = i

print(min_idx)
