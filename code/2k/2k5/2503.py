import heapq
from typing import *


class HeapDict:
    def __init__(self):
        self.heap = []
        self.dict = {}

    def push(self, cost, value):
        if cost not in self.dict:
            heapq.heappush(self.heap, cost)
            self.dict[cost] = []
        self.dict[cost].append(value)

    def pop(self) -> tuple[int, list]:
        if not self.heap:
            return []
        cost = heapq.heappop(self.heap)
        res = self.dict.pop(cost)
        return cost, res

    def __bool__(self):
        return bool(self.heap)


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

    def popTile(self, i: int, j: int, new_v=0):
        line = self.core[i]
        v = line[j]
        line[j] = new_v
        return v

    def getNeigh(self, i: int, j: int):
        return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    def getValidNeigh(self, el: tuple, sentinel: int, curval: int, curlist: list, nexdict: dict):
        neighlist = self.getNeigh(*el)
        for nel in neighlist:
            val = self.popTile(*nel, new_v=sentinel)
            if val == sentinel:
                continue
            print(nel,val)
            if val == curval:
                curlist.append(nel)
                continue
            nexdict[nel]=val
        return

    def getNumberCoverage(self, numbers: list[int], sentinel: int):
        numbers.append(sentinel)
        numbers.sort(reverse=True)
        curheap = HeapDict()
        cur = 0, 0
        curcost = self.popTile(*cur,new_v=sentinel)
        curheap.push(curcost, cur)
        res = {}
        acc = 0
        while curheap:
            cost, curlist = curheap.pop()
            while numbers[-1] <= cost:
                cur = numbers.pop()
                res[cur] = acc
            nexdict = {}
            while curlist:
                cur = curlist.pop()
                acc += 1
                self.getValidNeigh(cur, sentinel, cost, curlist, nexdict)
            for nex, cost in nexdict.items():
                curheap.push(cost, nex)
        return res


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        grid = Grid(grid)
        grid: Grid
        grid.sentinels(1000001)
        unique_queries = list(set(queries))
        res_dict: dict = grid.getNumberCoverage(unique_queries, 1000001)
        res = [res_dict[e] for e in queries]
        return res

    main = maxPoints


TESTS = [
    (
        ([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]),
        "test"
    )
    ,
    (
        ([[5,2,1],[1,1,2]], [3]),
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
