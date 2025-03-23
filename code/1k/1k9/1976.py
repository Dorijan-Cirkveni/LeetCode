import heapq
from collections import defaultdict
from heapq import heappush
from typing import *


class HeapDict:
    def __init__(self):
        self.heap: list = []
        self.dict: dict = {}

    def push(self, cost, key, value):
        if cost not in self.dict:
            heapq.heappush(self.heap, cost)
            self.dict[cost] = defaultdict(int)
        self.dict[cost][key] += value

    def pop(self):
        if not self.heap:
            return []
        cost = heapq.heappop(self.heap)
        res = self.dict.pop(cost)
        return cost, res

    def __bool__(self):
        return len(self.heap) != 0


class Graph:
    def __init__(self, links: dict = None):
        self.links = links if links else {}

    def addLink(self, a, b, v):
        self.links.setdefault(a, {})[b] = v
        self.links.setdefault(b, {})[a] = v

    def addLinks(self, links: list):
        for link in links:
            self.addLink(*link)

    def getNextsFor(self, cur: int, cur_cost: int, count: int, used: set, next_costs: HeapDict):
        for nex, delta in self.links[cur].items():
            if nex in used:
                continue
            new_cost = delta + cur_cost
            next_costs.push(new_cost, nex, count)

    def checkIfPathExists(self, start, end):
        used = set()
        curset = {start}
        while curset:
            used |= curset
            if end in curset:
                return True
            nexset = set()
            for cur in curset:
                nexset |= set(self.links.get(cur, {})) - used
            curset = nexset
        return False

    def findPathCount(self, start: int, end: int):
        if start == end:
            return 1
        used = set()
        next_costs = HeapDict()
        next_costs.push(0, start, 1)
        while next_costs:
            cur_cost, counts = next_costs.pop()
            if end in counts:
                return counts[end]
            used |= set(counts)
            for cur, count in counts.items():
                self.getNextsFor(cur, cur_cost, count, used, next_costs)
        return 0


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = Graph()
        graph.addLinks(roads)
        roads = None
        if not graph.checkIfPathExists(0, n - 1):
            return 0
        res = graph.findPathCount(0, n - 1)
        return res % (10 ** 9 + 7)

    main = countPaths


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
