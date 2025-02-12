from typing import *


def digitSum(n):
    res = 0
    while n:
        n, r = divmod(n, 10)
        res += r
    return res


def bestValues(L: list[int], new: int):
    for i, e in enumerate(L):
        if new > e:
            L[i] = new
            new = e


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        by_sum = {}
        while nums:
            num = nums.pop()
            dig = digitSum(num)
            lis = by_sum.setdefault(dig, [-1337] * 2)
            bestValues(lis, num)
        res = -1
        for lis in by_sum.values():
            if lis[-1]<0:
                continue
            res = max(res, sum(lis))
        return res

    main = maximumSum


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
