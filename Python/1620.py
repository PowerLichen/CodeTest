#1620: 나는야 포켓몬 마스터 이다솜
#풀이: 리스트와 딕셔너리를 사용.

from sys import stdin

n, m = map(int, stdin.readline().split())

p_names = ['null']
p_dict = dict()

for i in range(1,n+1):
    pokemon = stdin.readline().strip()
    p_names.append(pokemon)
    p_dict[pokemon] = i

#쿼리실행
for _ in range(m):
    target = stdin.readline().strip()
    if target.isdigit():
        print(p_names[int(target)])
    else:
        print(p_dict[target])


