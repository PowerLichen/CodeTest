'''
118669: 등산 코스 정하기
DFS를 이용하여 풀이.
'''

# import heapq

# VALUE_N_MAX = 50001
# VALUE_INTENSITY_MAX = 10000001


# def find_road(p_dict, gates, visit, start, cur, intensity, cur_max):
#     if cur in gates:
#         cur_max[0], cur_max[1] = start, intensity
#         return

#     nexts = p_dict[cur][:]
#     while nexts:
#         n_value, nxt = heapq.heappop(nexts)
#         if visit[nxt] == True:
#             continue
#         if n_value >= cur_max[1]:
#             break

#         visit[nxt] = True
#         find_road(p_dict, gates, visit, start, nxt,
#                   max(n_value, intensity), cur_max)
#         visit[nxt] = False

#     return


# def solution(n, paths, gates, summits):
#     answer = [VALUE_N_MAX, VALUE_INTENSITY_MAX]
#     p_dict = {i: list() for i in range(1, n+1)}
#     visit = [False for _ in range(n+1)]

#     gates = set(gates)
#     summits.sort()

#     for path in paths:
#         heapq.heappush(p_dict[path[0]], (path[2], path[1]))
#         heapq.heappush(p_dict[path[1]], (path[2], path[0]))

#     for i in summits:
#         visit[i] = True

#     for i in summits:
#         find_road(p_dict, gates, visit, i, i, 0, answer)

#     return answer


# TODO: -summit인 길은 이미 들렀던 길로 처리했을 때, intensity가 증가한 다음에는 어떻게 방문 체크를 하는가? 
# def bfs(p_dict, gates, summits, visit, summit, intencity):
#     queue = [summit]
#     while queue:
#         cur = queue.pop(0)

#         if cur in gates:
#             return True

#         flag = False
#         for n_value, nxt in p_dict[cur]:
#             # 아직 허용되지 않은 길
#             if n_value > intencity:
#                 flag = True
#                 continue
#             # 근처를 전부 방문하고, 더 낮은 값의 산봉우리가 왔던 경우
#             if visit[nxt] < 0 and visit[nxt] >= -summit:
#                 continue
#             # 다른 산봉우리
#             if nxt in summits:
#                 continue
#             if visit[nxt] == summit:
#                 continue

#             queue.append(nxt)

#         if flag == True:
#             visit[cur] = summit
#         else:
#             visit[cur] = -summit

#     return False

from collections import deque

VALUE_N_MAX = 50001
VALUE_INTENSITY_MAX = 10000001


def solution(n, paths, gates, summits):
    answer = [VALUE_N_MAX, VALUE_INTENSITY_MAX]
    p_dict = {i: list() for i in range(1, n+1)}
    visit = [0 for _ in range(n+1)]
    summit_queue = dict()

    gates = set(gates)
    summit_set = set(summits)

    summits.sort()

    for path in paths:
        p_dict[path[0]].append((path[2], path[1]))
        p_dict[path[1]].append((path[2], path[0]))

    for i in summits:
        visit[i] = i
        summit_queue[i] = deque([i])

    intencity = 1
    while True:
        for summit in summits:            
            queue = summit_queue[summit]
            nxt_summit_queue = deque()

            while queue:
                cur = queue.popleft()
                if cur in gates:
                    return [summit, intencity]
                
                flag = False
                for n_value, nxt in p_dict[cur]:
                    if n_value > intencity:
                        flag = True
                        continue
                    if nxt in summit_set:
                        continue
                    if visit[nxt] == summit:
                        continue
                    if visit[nxt] < 0 and visit[nxt] >= -summit:
                        continue

                    queue.append(nxt)

                if flag == True:
                    visit[cur] = summit
                    nxt_summit_queue.append(cur)
                else:
                    visit[cur] = -summit

            summit_queue[summit] = nxt_summit_queue

        intencity += 1

    return answer