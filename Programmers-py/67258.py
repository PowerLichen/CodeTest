# from collections import defaultdict

# def solution(gems):
#     gem_length = len(gems)
#     total_gem = len(set(gems))
#     count_dict = defaultdict(int)

#     start = 0
#     end = 1
#     count_dict[gems[0]] = 1

#     answer = [-1,-1]
#     gem_range = 100001
#     while start < end:
#         if len(count_dict) == total_gem:
#             cur_range = end - start
#             if cur_range < gem_range:
#                 gem_range = cur_range
#                 answer[0] = start
#                 answer[1] = end
            
#             target_gem = gems[start]
#             if count_dict[target_gem] == 1:
#                 count_dict.pop(target_gem)
#             else:
#                 count_dict[target_gem] -= 1

#             start += 1
#             continue
        
#         if end == gem_length:
#             break
#         count_dict[gems[end]] += 1
#         end += 1

#     answer[0] += 1
#     return answer





from collections import defaultdict

def solution(gems):
    total_gem_cnt = len(set(gems))
    count_dict = defaultdict(int)

    start = 0

    answer = [-1,-1]
    gem_range = 100001
    for end, gem in enumerate(gems, start=1):
        count_dict[gem] += 1
        while len(count_dict) == total_gem_cnt:
            cur_range = end - start
            if cur_range < gem_range:
                gem_range = cur_range
                answer[0] = start
                answer[1] = end

            target_gem = gems[start]
            if count_dict[target_gem] == 1:
                count_dict.pop(target_gem)
            else:
                count_dict[target_gem] -= 1

            start += 1

    answer[0] += 1
    return answer
            


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])