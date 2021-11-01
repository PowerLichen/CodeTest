#1764: 듣보잡
#풀이법: 셋을 이용하여 각각의 경우에 해당하는 이름을 저장하고 교집합을 이용한 코드를 작성.
n, m = map(int, input().split())
not_hear = set()
not_seen = set()

for i in range(n):
    not_hear.add(input())
for i in range(m):
    not_seen.add(input())

result = sorted(not_hear & not_seen)

print(len(result))
for name in result:
    print(name)
