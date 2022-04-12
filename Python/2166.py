# 2166: 다각형의 면적
# 처음 한 점을 잡고 벡터의 외적을 이용해서 삼각형들의 넓이를 모두 더하기

def calc_area(result, cur_x, cur_y, next_x, next_y):
    result = ()

    pass

n = int(input())

result = 0.0

x, y = map(int,input().split())
cur_x, cur_y = map(int,input().split())

for _ in range(n-2):
    next_x, next_y = map(int,input().split())
    # 외적 계산
    temp = (cur_x - x) * (next_y - y) - (cur_y - y) * (next_x - x)
    temp /= 2.0
    result += temp
    cur_x, cur_y = next_x, next_y


if result < 0:
    result *= -1

print(f'{result:.1f}')

    
