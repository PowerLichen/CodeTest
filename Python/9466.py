# 9466: 텀 프로젝트
# 팀원 상황을 [0: 미정, -1: 팀없음 확실, 1: 팀원 확실]으로 상태 확인.
# 팀원 한명씩 돌아가면서 확인을 하는데, 순환을 찾으면 순환부분만 1로 변경, 나머지는 -1로 변경하도록 구현.
# 팀원이 되지 못하는 경우에는 -1로 전부 순환

def check_circular(survey, check, start):
    cur = start
    circular_set = set()
    circular_set.add(start)

    while True:
        cur = survey[cur]

        # 팀원이 되지 못하는 경우
        if check[cur] != 0:
            # 순환 다시 돌아서 -1로 변경
            while start != cur and check[start] == 0:
                check[start] = -1
                start = survey[start]
            return

        # 순환을 찾았을 경우
        if cur in circular_set:
            # 순환은 전부 1로 변경
            check[cur] = 1
            inner_cir_start = survey[cur]
            while cur != inner_cir_start:
                check[inner_cir_start] = 1
                inner_cir_start = survey[inner_cir_start]

            # 순환이 아닌 부분은 -1로 변경
            if check[start] == 0:
                cur = start
                check[cur] = -1
                least_num = survey[cur]
                while check[least_num] == 0:
                    check[least_num] = -1
                    least_num = survey[least_num]

            return

        circular_set.add(cur)


def make_team():
    n = int(input())
    survey = [0] + list(map(int, input().split()))
    # 0: 미정, -1: 팀없음 확실, 1: 팀원 확실
    check = [0] * (n+1)
    check[0] = 1

    for i in range(1, n+1):
        if check[i] != 0:
            continue

        if survey[i] == i:
            check[i] = 1
            continue

        check_circular(survey, check, i)

    print(check.count(-1))


t = int(input())

for _ in range(t):
    make_team()
