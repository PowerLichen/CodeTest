from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for src, dest in tickets:
        graph[src].append(dest)

    for key in graph.keys():
        graph[key].sort(reverse=True)

    answer = list()
    stack = ["ICN"]
    while stack:
        cur = stack[-1]
        if len(graph[cur]) > 0:
            stack.append(graph[cur].pop())
        else:
            answer.append(stack.pop())

    answer.reverse()
    return answer