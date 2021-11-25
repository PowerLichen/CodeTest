# 1043: 거짓말

result = 0
people_n, party_n = map(int, input().split())
avoids = list(map(int, input().split()))[1:]
partys = list()

data = dict()
for i in range(1, people_n+1):
    data[i] = list()

for i in range(party_n):
    temp = list(map(int, input().split()))[1:]
    partys.append(temp)
    for n in temp:
        data[n].append(i)

check = [False for i in range(people_n+1)]
while len(avoids) > 0:
    cur = avoids.pop(0)
    hired_idxs = data[cur]
    for idx in hired_idxs:
        for nxt in partys[idx]:
            if check[nxt] == False:
                check[nxt] = True
                avoids.append(nxt)


avoids = [i for i in range(1,people_n+1) if check[i] == True]

for party in partys:
    if len(party) == 0:
        continue
    party = set(party)
    avoids = set(avoids)
    if len(party) == len(party - avoids):
        result += 1

print(result)

# for i in range(party_n):
#     temp = list(map(int, input().split()))
#     arr = temp[1:]
#     check = False
#     for n in avoids:
#         if n in arr:
#             check = True
#             break

#     partys.append((temp[0], check, set(arr)))

# partys.sort(key=lambda x: (x[0],x[1]), reverse=True)

# for party in partys:
#     checklist = party[2]
#     if len(checklist) != len(checklist - avoids):
#         avoids.update(checklist)

# for party in partys:
#     checklist = party[2]
#     if party[0] == 0:
#         continue
#     if len(checklist) == len(checklist - avoids):
#         result += 1

# print(result)
