'''
118669: 등산 코스 정하기
DFS를 이용하여 풀이.
'''

import heapq

VALUE_N_MAX = 50001
VALUE_INTENSITY_MAX = 10000001


def find_road(p_dict, gates, visit, start, cur, intensity, cur_max):
    if cur in gates:
        cur_max[0], cur_max[1] = start, intensity
        return

    nexts = p_dict[cur][:]
    while nexts:
        n_value, nxt = heapq.heappop(nexts)
        if visit[nxt] == True:
            continue
        if n_value >= cur_max[1]:
            break

        visit[nxt] = True
        find_road(p_dict, gates, visit, start, nxt,
                  max(n_value, intensity), cur_max)
        visit[nxt] = False

    return


def solution(n, paths, gates, summits):
    answer = [VALUE_N_MAX, VALUE_INTENSITY_MAX]
    p_dict = {i: list() for i in range(1, n+1)}
    visit = [False for _ in range(n+1)]

    gates = set(gates)
    summits.sort()

    for path in paths:
        heapq.heappush(p_dict[path[0]], (path[2], path[1]))
        heapq.heappush(p_dict[path[1]], (path[2], path[0]))

    for i in summits:
        visit[i] = True

    for i in summits:
        find_road(p_dict, gates, visit, i, i, 0, answer)

    return answer

