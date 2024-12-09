from collections import deque
from typing import *
import inspect


def pop_next(DQ, start, value):
    if DQ[0][0] >= start:
        return 0
    cur = None
    DQ.append((start+1,0))
    while DQ[0][0] < start:
        cur = DQ.popleft()
    DQ.appendleft(cur)
    DQ.pop()
    return cur[1] + value


def append_next(DQ:deque, end, value):
    temp = [(float('inf'), 0)]
    DQ.appendleft((0,0))
    while DQ[-1][1] > value:
        temp.append(DQ.pop())
    while DQ[-1][0] >= end:
        DQ.pop()
    if temp[-1][0] > end:
        DQ.append((end, value))
    while temp:
        DQ.append(temp.pop())
    DQ.pop()
    DQ.popleft()


class Solution:
    def __init__(self):
        self.best = None
        self.DQ = None

    def step(self, start, end, value):
        DQ = self.DQ
        best = pop_next(self.DQ, start, value)
        if self.best < best:
            self.best = best
        append_next(self.DQ, end, value)
        return

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=tuple, reverse=True)
        self.DQ = deque([
            (0, 0),
            (float('inf'), 0)
        ])
        self.best = 0
        while events:
            self.step(*events.pop())
        return self.best

    main = maxTwoEvents


TESTS = [
    (
        (
            [[1,3,2],[4,5,2],[2,4,3]],
        ),
        4)
    ,
    (
        (
            [[1,3,2],[4,5,2],[1,5,5]],
        ),
        5)
    ,
    (
        (
            [[1,5,3],[1,5,1],[6,6,5]],
        ),
        8)
    ,

        (
        (
            [[10,83,53],[63,87,45],[97,100,32],[51,61,16]],
        ),
        5)
    ,
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
