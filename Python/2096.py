# 2096: 내려가기
# 각 위치의 최대 점수와 최소 점수를 저장하는 리스트를 만들고,
# 각 위치에 대해서 가능한 최대, 최소값을 저장한다. 
# 메모리 제한이 있으므로 입력을 받을때마다 계산을 수행한다.


n = int(input())

a, b, c = map(int, input().split())
largest = [a, b, c]
smallest = [a, b, c]

for _ in range(n - 1):
    numbers = list(map(int, input().split()))
    temp = [0, 0, 0]

    # 다음 최대값 계산
    temp[0] = max(largest[0], largest[1]) + numbers[0]
    temp[1] = max(largest) + numbers[1]
    temp[2] = max(largest[1], largest[2]) + numbers[2]
    for i in range(3):
        largest[i] = temp[i]
    
    # 다음 최소값 계산
    temp[0] = min(smallest[0], smallest[1]) + numbers[0]
    temp[1] = min(smallest) + numbers[1]
    temp[2] = min(smallest[1], smallest[2]) + numbers[2]
    for i in range(3):
        smallest[i] = temp[i]

print(max(largest), min(smallest))
