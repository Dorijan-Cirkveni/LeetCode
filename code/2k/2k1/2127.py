import collections
from dataclasses import dataclass
from typing import *


@dataclass
class Merge:
    count: int
    best: int


class Solution:
    def __init__(self):
        self.starts: list[tuple[int, int]] = []
        self.merges: dict[int, Merge] = {}
        self.favorite: list[int] = []

    def findMergesAndStarts(self) -> None:
        counts = [0] * len(self.favorite)
        circle = True
        for e in self.favorite:
            if counts[e]:
                circle = False
            counts[e] += 1
        if circle:
            return
        self.merges = {}
        self.starts = []
        i = len(counts)
        while counts:
            i -= 1
            cur = counts.pop()
            if cur == 1:
                continue
            if cur == 0:
                self.starts.append((i, 0))
                continue
            self.merges[i] = Merge(cur, 0)

    def seekCycle(self, start: int):
        cur = start
        tempcount = 0
        while cur not in self.merges:
            cur = self.favorite[cur]
            tempcount += 1
            if cur == start:
                break
        return cur, tempcount

    def maximumInvitations(self, favorite: List[int]) -> int:
        self.favorite = favorite
        self.findMergesAndStarts()
        if not self.merges:
            return len(self.favorite)
        res = 0
        while self.starts:
            start, count = self.starts.pop()
            cur, delta_res = self.seekCycle(start)
            cur: int
            delta_res: int
            if cur == start:
                res += delta_res
                break
            count += delta_res
            mcur = self.merges[cur]
            mcur.count -= 1
            if count > mcur.best:
                mcur.best = count
            if not mcur.count:
                self.merges.pop(cur)
                self.starts.append((cur, mcur.best))
        merges: list = list(self.merges)
        while self.merges:
            cur = merges.pop()
            mer: Merge = self.merges.pop(cur)
            _, delta_res = self.seekCycle(cur)
            res += delta_res + mer.best
        return res

    main = maximumInvitations


TESTS = [
    (
        ([3, 0, 1, 4, 1],),
        4
    )
    ,
    (
        ([2, 2, 1, 2],),
        3
    )
    ,
    (
        ([3, 0, 1, 4, 1],),
        4
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
