from typing import *


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_acc = [0] * len(grid[0])
        col_acc = []
        for row in grid:
            cur = 0
            for i, e in enumerate(row):
                if e == 0:
                    continue
                cur += 1
                row_acc[i] += 1
            col_acc.append(cur)
        res = 0
        for i, line in enumerate(grid):
            if col_acc[i] >= 2:
                res += col_acc[i]
                continue
            for j, el in enumerate(line):
                if not el:
                    continue
                res += row_acc[j] >= 2
        return res

    main = countServers


TESTS = [
    (
        ([[1, 0], [0, 1]],),
        0
    )
    ,
    (
        ([[1, 0], [1, 1]],),
        3
    )
    ,
    (
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]],),
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
