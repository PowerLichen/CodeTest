# 1644: 소수의 연속합
# n 이하의 소수를 전부 구하고, start와 end를 이용해서 좌우를 하나씩 빼고 더하는 것으로 답을 계산하도록 구현
n = int(input())
prime_check = [False, False] + [True] * (n-1)
primes = list()

for i in range(2, n+1):
    if prime_check[i] == True:
        primes.append(i)
        for j in range(i*2, n+1, i):
            prime_check[j] = False

answer = 0
start, end = 0, 0
sum_value = 0
max_cnt = len(primes)

while end <= max_cnt:
    if sum_value == n:
        answer += 1

    if sum_value <= n:
        if end == max_cnt:
            break
        sum_value += primes[end]
        end += 1
    else:
        sum_value -= primes[start]
        start += 1


print(answer)
