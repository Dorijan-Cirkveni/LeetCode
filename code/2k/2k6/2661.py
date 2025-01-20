from collections import defaultdict
from typing import *


def occurrences(mat):
    res = {}
    for i, line in enumerate(mat):
        for j, el in enumerate(line):
            res[el] = i, j
        mat[i] = None
    return res


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        if 1 in (n, m):
            return 0
        rows = defaultdict(int)
        cols = defaultdict(int)
        occ = occurrences(mat)
        mat = None
        _ = mat
        res = 0
        for res, e in enumerate(arr):
            i, j = occ.pop(e)
            rows[i] += 1
            if rows[i] == m:
                break
            cols[j] += 1
            if cols[j] == n:
                break
        return res

    main = firstCompleteIndex


TESTS = [
    (
        ([0, 1], [[0, 1]]),
        0
    )
    ,
    (
        ([4, 2, 3, 1], [[1, 2], [4, 3]]),
        2
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
