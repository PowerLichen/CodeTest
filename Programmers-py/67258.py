"""
67258: 보석 쇼핑
풀이:
처음부터 모든 보석이 포함될 때 까지의 start, end를 찾고,
보석이 전부 포함되어 있으면 start를 증가, 아니라면 end를 증가.
"""

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