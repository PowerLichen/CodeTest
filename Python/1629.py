# 1629: 곱셈
# square and multuply를 사용

a, b, c = map(int, input().split())

result = 1
while b > 0:
    if b & 1 == 1:
        result = (result*a) % c
    a = (a*a) % c
    b = b >> 1


print(result)
