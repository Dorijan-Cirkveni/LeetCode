import heapq


class HeapDict:
    def __init__(self):
        self.heap = []
        self.dict = {}

    def push(self, cost, value):
        if cost not in self.dict:
            heapq.heappush(self.heap, cost)
            self.dict[cost] = []
        self.dict[cost].append(value)

    def pop(self):
        if not self.heap:
            return []
        cost = heapq.heappop(self.heap)
        res = self.dict.pop(cost)
        return cost, res

    def __bool__(self):
        return bool(self.heap)


def main():
    return


if __name__ == "__main__":
    main()
