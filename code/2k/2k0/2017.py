from typing import *


def accList(L: list):
    acc = 0
    for i, e in enumerate(L):
        L[i] = acc
        acc += e


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        lower_sum = grid.pop()
        accList(lower_sum)
        best = lower_sum[-1]
        upper_sum = 0
        while lower_sum:
            best = min(best, max(lower_sum[-1], upper_sum))
            lower_sum.pop()
            upper_sum += grid[0].pop()
        return best

    main = gridGame


TESTS = [
    (
        ([[2, 5, 4], [1, 5, 1]],),
        4
    )
    ,
    (
        ([[3, 3, 1], [8, 5, 2]],),
        4
    )
    ,
    (
        ([[1,3,1,15],[1,3,3,1]],),
        7
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
