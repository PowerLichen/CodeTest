#7662: 이중 우선순위 큐
#이진검색을 이용하여 정렬된 상태로 삽입하고 결과를 확인하도록 작성했지만 시간초과

class Duelpq:
    def __init__(self):
        self.items = list()

    def insert(self, value):
        start = 0
        end = len(self.items) - 1

        while start <= end:
            mid = (start+end)//2
            if self.items[mid] < value:
                start = mid+1
            else:
                end = mid-1
        
        self.items.insert(start, value)

    def pop(self):
        return self.items.pop(0)

    def rpop(self):
        return self.items.pop()


t = int(input())

for _ in range(t):
    k = int(input())
    dpq = Duelpq()
    for _ in range(k):
        cmd, num = input().split()
        if cmd == "I":
            dpq.insert(int(num))
        elif len(dpq.items) > 0:
            if num == "-1":
                dpq.pop()
            else:
                dpq.rpop()
    
    if len(dpq.items) > 0:
        print(dpq.items[-1], dpq.items[0])
    else:
        print('EMPTY')


            

