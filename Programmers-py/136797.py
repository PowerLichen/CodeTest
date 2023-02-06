def update_case(cases, pos, cur_cost):
    prev_cost = cases.get(pos)
    if (prev_cost is None) or (prev_cost > cur_cost):
        cases[pos] = cur_cost
        
        
def solution(numbers):
    move_costs = (
        (1, 7, 6, 7, 5, 4, 5, 3, 2, 3),
        (7, 1, 2, 4, 2, 3, 5, 4, 5, 6),
        (6, 2, 1, 2, 3, 2, 3, 5, 4, 5),
        (7, 4, 2, 1, 5, 3, 2, 6, 5, 4),
        (5, 2, 3, 5, 1, 2, 4, 2, 3, 5),
        (4, 3, 2, 3, 2, 1, 2, 3, 2, 3),
        (5, 5, 3, 2, 4, 2, 1, 5, 3, 2),
        (3, 4, 5, 6, 2, 3, 5, 1, 2, 4),
        (2, 5, 4, 5, 3, 2, 3, 2, 1, 2),
        (3, 6, 5, 4, 5, 3, 2, 4, 2, 1)
    )
    
    cur_cases = {(4,6):0}
    for ch in numbers:
        num = int(ch)
        nxt_cases = dict()
        for pos, cost in cur_cases.items():
            pos_left, pos_right = pos
            
            if (num == pos_left) or (num == pos_right):
                update_case(nxt_cases, pos, cost + 1)
                continue
            
            pos = (num, pos_right)
            cur_cost = cost + move_costs[pos_left][num]
            update_case(nxt_cases, pos, cur_cost)
            
            pos = (pos_left, num)
            cur_cost = cost + move_costs[pos_right][num]
            update_case(nxt_cases, pos, cur_cost)

        cur_cases = nxt_cases

    return min(cur_cases.values())

# def solution(numbers):
#     move_costs = (
#         (1, 7, 6, 7, 5, 4, 5, 3, 2, 3),
#         (7, 1, 2, 4, 2, 3, 5, 4, 5, 6),
#         (6, 2, 1, 2, 3, 2, 3, 5, 4, 5),
#         (7, 4, 2, 1, 5, 3, 2, 6, 5, 4),
#         (5, 2, 3, 5, 1, 2, 4, 2, 3, 5),
#         (4, 3, 2, 3, 2, 1, 2, 3, 2, 3),
#         (5, 5, 3, 2, 4, 2, 1, 5, 3, 2),
#         (3, 4, 5, 6, 2, 3, 5, 1, 2, 4),
#         (2, 5, 4, 5, 3, 2, 3, 2, 1, 2),
#         (3, 6, 5, 4, 5, 3, 2, 4, 2, 1)
#     )
    
#     cur_cases = {(4,6):0}
#     nxt_cases = dict()
#     get_value_in_pos = nxt_cases.get
#     for ch in numbers:
#         num = int(ch)
#         nxt_cases = dict()
#         for pos, cost in cur_cases.items():
#             pos_left, pos_right = pos

#             cur_cost = nxt_cases.get(pos)
#             calc_cost = cost + 1
#             if (num == pos_left) or (num == pos_right):
#                 if (cur_cost == None) or (cur_cost > calc_cost):
#                     nxt_cases[pos] = calc_cost
#                 continue
            
#             pos = (num, pos_right)
#             cur_cost = nxt_cases.get(pos)
#             calc_cost = cost + move_costs[pos_left][num]
#             if (cur_cost == None) or (cur_cost > calc_cost):
#                 nxt_cases[pos] = calc_cost
            
#             pos = (pos_left, num)
#             cur_cost = nxt_cases.get(pos)
#             calc_cost = cost + move_costs[pos_right][num]
#             if (cur_cost == None) or (cur_cost > calc_cost):
#                 nxt_cases[pos] = calc_cost

#         cur_cases = nxt_cases

#     return min(cur_cases.values())


# MAX_VALUE = 1000000

# 더 깔끔하지만 min이 더 오래걸림
# def solution(numbers):
#     move_costs = (
#         (1, 7, 6, 7, 5, 4, 5, 3, 2, 3),
#         (7, 1, 2, 4, 2, 3, 5, 4, 5, 6),
#         (6, 2, 1, 2, 3, 2, 3, 5, 4, 5),
#         (7, 4, 2, 1, 5, 3, 2, 6, 5, 4),
#         (5, 2, 3, 5, 1, 2, 4, 2, 3, 5),
#         (4, 3, 2, 3, 2, 1, 2, 3, 2, 3),
#         (5, 5, 3, 2, 4, 2, 1, 5, 3, 2),
#         (3, 4, 5, 6, 2, 3, 5, 1, 2, 4),
#         (2, 5, 4, 5, 3, 2, 3, 2, 1, 2),
#         (3, 6, 5, 4, 5, 3, 2, 4, 2, 1)
#     )
    
#     cur_cases = {(4,6):0}
#     for ch in numbers:
#         num = int(ch)
#         nxt_cases = dict()
#         for pos, cost in cur_cases.items():
#             pos_left, pos_right = pos
            
#             cur_cost = nxt_cases.get(pos, MAX_VALUE)
#             if (num == pos_left) or (num == pos_right):
#                 nxt_cases[pos] = min(cur_cost, cost+1)
#                 continue
            
#             pos = (num, pos_right)
#             cur_cost = nxt_cases.get(pos, MAX_VALUE)
#             nxt_cases[pos] = min(cur_cost, cost + move_costs[pos_left][num])
            
#             pos = (pos_left, num)
#             cur_cost = nxt_cases.get(pos, MAX_VALUE)
#             nxt_cases[pos] = min(cur_cost, cost + move_costs[pos_right][num])

#         cur_cases = nxt_cases

#     return min(cur_cases.values())


