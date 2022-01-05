# 1927: 최소 힙
# 최소 힙 구조를 클래스로 구현

from sys import stdin


class Minheap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items)-1

    def _calc_push(self):
        i = len(self)
        parent = i//2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def _calc_pop(self):
        i = 1
        while True:
            left = i*2
            right = i*2+1
            curIdx = i

            if left <= len(self) and self.items[left] < self.items[curIdx]:
                curIdx = left
            if right <= len(self) and self.items[right] < self.items[curIdx]:
                curIdx = right
            if i == curIdx:
                break
            self.items[i], self.items[curIdx] = self.items[curIdx], self.items[i]
            i = curIdx

    def push(self, value):
        self.items.append(value)
        self._calc_push()

    def pop(self):
        if len(self) == 0:
            return 0

        root = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._calc_pop()

        return root


calc = Minheap()

n = int(stdin.readline())

for _ in range(n):
    cmd = int(stdin.readline())
    if cmd == 0:
        print(calc.pop())
    else:
        calc.push(cmd)
