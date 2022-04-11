import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solution(nums):
    length = len(nums)
    if length <= 1:
        return nums
    
    for i in range(1,length):
        if nums[i] > nums[0]:
            return solution(nums[1:i]) + solution(nums[i:]) + [nums[0]]

    return solution(nums[1:]) + [nums[0]]

nums = list()
while True:
    try:
        nums.append(int(input()))
    except:
        break

nums = solution(nums)

for n in nums:
    print(n)
