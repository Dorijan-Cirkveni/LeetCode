import heapq
from typing import *

INF = 1 << 31
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def offset(i: int, j: int, d: int):
    di, dj = DIRECTIONS[d]
    return i + di, j + dj


class PrioritySetQueue:
    def __init__(self):
        self.priorities: list[int] = []
        self.values: dict[int, set] = {}

    def add(self, index, value):
        if index not in self.values:
            heapq.heappush(index)
            self.values[index] = {value}
            return
        self.values[index].add(value)

    def __bool__(self):
        return bool(self.priorities)

    def pop(self):
        key = heapq.heappop(self.priorities)
        values = self.values.pop(key)
        return key, list(values)


def listBorderTiles(n: int, m: int):
    temp = []
    temp += [(i, 0) for i in range(n - 1)]
    temp += [(0, i) for i in range(1, m)]
    temp += [(i, m - 1) for i in range(1, n)]
    temp += [(n - 1, i) for i in range(m - 1)]
    return temp


class Solution:
    def __init__(self):
        self.queue = None
        self.m = 0
        self.n = 0
        self.grid:list[list[int]] = []

    def get(self, i, j):
        return self.grid[i][j]

    def border(self):
        for e in self.grid:
            e.append(INF)
        self.grid.append([INF]*self.m)

    def get_neigh(self,tile):
        res=[]
        for i in range(4):
            nex=offset(*tile,)

    def set_nexts(self):
        temp = listBorderTiles(self.n, self.m)
        while temp:
            tile = temp.pop()
            v = self.get(*tile)
            self.queue.add(v, tile)
        return

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.grid = heightMap
        self.n = len(heightMap)
        self.m = len(heightMap[0])
        self.queue = PrioritySetQueue()
        self.set_nexts()
        while self.queue:
            height, values = self.queue.pop()
            while values:


    main = trapRainWater


TESTS = [
    (
        ([0, 1], 1),
        "test"
    )
    ,
    (
        ([0, 1], 2),
        "also test"
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
    for i, (args, true_res) in enumerate(tests):
        res = SOL.main(*args)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1}")
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
