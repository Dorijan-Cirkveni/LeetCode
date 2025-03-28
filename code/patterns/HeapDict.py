import heapq
from heapq import heappop


class HeapDict:
    def __init__(self):
        self.heap = []
        self.dict = {}

    def push(self, cost, value):
        if cost not in self.dict:
            heapq.heappush(cost)
            self.dict[cost] = []
        self.dict[cost].append(value)

    def pop(self):
        if not self.heap:
            return []
        cost = heapq.heappop(self.heap)
        res = self.dict.pop(cost)
        return res


def main():
    return


if __name__ == "__main__":
    main()
