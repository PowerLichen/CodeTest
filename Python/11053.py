from bisect import bisect
import imp
import sys
import bisect
input = sys.stdin.readline

length = int(input())

nums = [0] + list(map(int, input().split()))

dp = [0]


for i in range(1, length+1):
    cur_num = nums[i]
    if cur_num > dp[-1]:
        dp.append(cur_num)
    else:
        idx = bisect.bisect_left(dp, cur_num)
        dp[idx] = cur_num

print(len(dp)-1)

