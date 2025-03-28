import heapq
from typing import *


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


class Grid:
    def __init__(self, core: list[list], deepcopy=False):
        if deepcopy:
            core = [[f for f in e] for e in core]
        self.n = len(core)
        self.m = len(core[0])
        self.core = core

    def sentinels(self, value: int, width: int = 1):
        for e in self.core:
            e += [value] * width
        self.core += [[value] * (self.m + width)] * width

    def getTile(self, i, j):
        return self.core[i][j]

    def setTile(self, i, j, v):
        self.core[i][j] = v

    def popTile(self, i: int, j: int, v=0):
        line = self.core[i]
        v = line[j]
        line[j] = 0
        return v

    def getNeigh(self, i: int, j: int):
        return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    def getValidNeigh(self, el: tuple, sentinels: set[int], output_method: callable):
        for nel in self.getNeigh(*el):
            val = self.getTile(*nel)
            if val in sentinels:
                continue
            output_method(nel)

    def getNumberCoverage(self,numbers:list[int]):
        numbers

    def clearIsland(self, start: tuple):
        curset = {start}
        res = 0
        while curset:
            nexset = set()
            for cur in curset:
                res += self.popTile(*cur)
                self.getValidNeigh(cur, sentinels={0}, output_method=nexset.add)
            curset = nexset
        return res



class Solution:
    """
    Solulu.
    """

    def __init__(self):
        self.test = "test"

    def Template(self, L: List, i: int):
        return self.test

    main = Template


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
