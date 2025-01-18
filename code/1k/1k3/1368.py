from typing import *

INF = 1 << 31
DIRECTIONS = [(0, 0),(0, 1),(0, -1),(1, 0),(-1, 0)]


def offset(i: int, j: int, d: int):
    di, dj = DIRECTIONS[d]
    return i + di, j + dj


class Solution:
    def __init__(self):
        self.costs = []
        self.directions = []

    def getCost(self, i, j):
        return self.costs[i][j]

    def setCosts(self, i, j, v):
        self.costs[i][j] = v

    def getFreeDir(self, i, j):
        return self.directions[i][j]

    def checkCurCost(self, cur: tuple, cost: int, cur_stack: list):
        if self.getCost(*cur) > cost:
            self.setCosts(*cur, v=cost)
            cur_stack.append(cur)

    def startCosts(self):
        self.costs = []
        line = []
        for line in self.directions:
            cur = [INF] * len(line)
            cur.append(-1)
            self.costs.append(cur)
        self.costs.append([-1] * len(line))

    def getCurAndNextNeigh(self, cur, cur_stack: list, nex_stack: list):
        cost: int = self.getCost(*cur)
        directions = {1, 2, 3, 4}

        free_dir: int = self.getFreeDir(*cur)
        directions.remove(free_dir)
        nex_loc = offset(*cur, d=free_dir)
        self.checkCurCost(nex_loc, cost, cur_stack)

        cost += 1
        for direct in directions:
            nex_loc = offset(*cur, d=direct)
            self.checkCurCost(nex_loc, cost, nex_stack)

    def traverse(self, start: tuple, goal: tuple):
        cur_stack = [start]
        self.setCosts(*start, v=0)
        nex_stack = []
        while cur_stack:
            cur = cur_stack.pop()
            if cur == goal:
                return self.getCost(*cur)
            self.getCurAndNextNeigh(cur, cur_stack, nex_stack)
            if not cur_stack:
                cur_stack = nex_stack
                nex_stack = []

    def minCost(self, grid: List[List[int]]) -> int:
        self.directions = grid
        self.startCosts()
        goal = len(grid) - 1, len(grid[0]) - 1
        res = self.traverse((0, 0), goal)
        return res

    main = minCost


TESTS = [
    (
        ([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]],),
        3
    )
    ,
    (
        ([[1,1,3],[3,2,2],[1,1,4]],),
        0
    )
    ,
    (
        ([[1,2],[4,3]],),
        1
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
