import heapq
from typing import *

INF = 1 << 31
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def offset(i: int, j: int, d: int):
    di, dj = DIRECTIONS[d]
    return i + di, j + dj


def listBorderTiles(n: int, m: int):
    n -= 1
    m -= 1
    temp = [(0, 0), (0, m), (n, 0), (n, m)]
    temp += [(i, 0) for i in range(1, n)]
    temp += [(0, i) for i in range(1, m)]
    temp += [(i, m) for i in range(1, n)]
    temp += [(n, i) for i in range(1, m)]
    return temp


class Solution:
    def __init__(self):
        self.visited = []
        self.queue = []
        self.m = 0
        self.n = 0
        self.grid: list[list[int]] = []

    def get(self, i, j):
        return self.grid[i][j]

    def getNeigh(self, i, j):
        res = []
        if i > 0:
            el = i - 1, j
            res.append(el)
        if i < self.n - 1:
            el = i + 1, j
            res.append(el)
        if j > 0:
            el = i, j - 1
            res.append(el)
        if j < self.m - 1:
            el = i, j + 1
            res.append(el)
        return res

    def set_nexts(self):
        temp = listBorderTiles(self.n, self.m)
        while temp:
            entry = 0, temp.pop()
            heapq.heappush(self.queue, entry)
        return

    def setVisited(self, i, j):
        self.visited[i][j] = True

    def getVisited(self, i, j):
        return self.visited[i][j]

    def step(self, height, cur):
        res = 0
        if self.getVisited(*cur):
            return 0
        self.setVisited(*cur)
        val = self.get(*cur)
        if height > val:
            res = height - val
            val = height
        neigh = self.getNeigh(*cur)
        while neigh:
            nex = neigh.pop()
            entry = val, nex
            if self.getVisited(*nex):
                continue
            heapq.heappush(self.queue, entry)
        return res

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.grid = heightMap
        self.n = len(heightMap)
        self.m = len(heightMap[0])
        self.visited = [[False] * self.m for _ in range(self.n)]
        self.queue = []
        self.set_nexts()
        res = 0
        while self.queue:
            height, cur = heapq.heappop(self.queue)
            res += self.step(height, cur)
        return res

    main = trapRainWater


TESTS = [
    (
        ([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]],),
        14
    )
    ,
    (
        ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]],),
        4
    )
    ,
    (
        ([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]],),
        10
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
    print(listBorderTiles(3, 6))
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
