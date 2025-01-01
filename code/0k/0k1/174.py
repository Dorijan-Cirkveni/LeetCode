from collections import deque
from typing import *
import inspect


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        last_list = [float('inf')] * len(dungeon[0])
        last_list[-1] = 1
        while dungeon:
            curlist = deque()
            last = float('inf')
            E = dungeon.pop()
            while E:
                e = E.pop()
                lastlast = last_list.pop()
                min_hp = min(last, lastlast)
                min_hp -= e
                if min_hp < 1:
                    min_hp = 1
                curlist.appendleft(min_hp)
                last = min_hp
            last_list = curlist
            print(last_list)
        return int(last_list[0])

    main = calculateMinimumHP


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
