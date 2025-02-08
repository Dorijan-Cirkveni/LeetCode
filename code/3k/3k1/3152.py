from typing import *
import inspect


def isAlternating(L: list[int]):
    L.reverse()
    RES = [0]
    last = L.pop()
    acc = 0
    while L:
        cur = L.pop()
        acc += (cur ^ last) & 1 == 1
        RES.append(acc)
        last = cur
    return RES


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        alts = isAlternating(nums)
        for i, (a, b) in enumerate(queries):
            res = (alts[b] - alts[a]) == b - a
            queries[i] = res
        queries: List[bool]
        return queries

    main = isArraySpecial


TESTS = [
    (
        ([0, 1], 1),
        "test")
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
    S = SepArray()
    return


if __name__ == "__main__":
    main()
