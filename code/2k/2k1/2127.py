import collections
from typing import *

from dataclasses import dataclass


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

    def step(self, cur):
        nex = self.favorite[cur]
        self.favorite[cur] = cur
        return nex

    def findDuos(self):
        duos = 0
        for i, e in enumerate(self.favorite):
            if i == e:
                continue
            duos += self.favorite[e] == i
        return duos

    def maximumInvitations(self, favorite: List[int]) -> int:
        self.favorite = favorite
        self.findMergesAndStarts()
        if not self.merges:
            return len(self.favorite)
        while self.starts:
            cur, count = self.starts.pop()
            delta_res = 0
            while cur not in self.merges:
                delta_res += 1
                cur = self.step(cur)
            count += delta_res
            mcur = self.merges[cur]
            if count > mcur.best:
                mcur.best = count
            mcur.count -= 1
            if not mcur.count:
                self.merges.pop(cur)
                self.starts.append((cur, mcur.best))
        merges: list = list(self.merges)
        res = 0
        merge_res = 0
        while merges:
            start = merges.pop()
            if start not in self.merges:
                continue
            cur = start
            mer: Merge = self.merges.pop(cur)
            cur = self.favorite[cur]
            delta_res = 1
            while cur != start:
                delta_res += 1
                cur = self.step(cur)
            cur = self.favorite[cur]
            self.favorite[start] = start
            if delta_res == 2:
                if cur in self.merges:
                    delta_res += self.merges.pop(cur).best
                merge_res += delta_res + mer.best
                continue
            if res < delta_res:
                res = delta_res
        if res < merge_res:
            res = merge_res
        res += self.findDuos()
        return res

    main = maximumInvitations


TESTS = [
    (
        ([3,0,1,4,1],),
        4
    )
    ,
    (
        ([1, 0, 3, 2, 5, 6, 7, 4, 9, 8, 11, 10, 11, 12, 10],),
        11
    )
    ,
    (
        ([2, 2, 1, 2],),
        3
    )
    ,
    (
        ([1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8],),
        6
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
