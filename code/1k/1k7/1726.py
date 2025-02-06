from collections import defaultdict
from typing import *


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums)<4:
            return 0
        singles = set()
        pairs = defaultdict(int)

        while nums:
            cur = nums.pop()
            for other in singles:
                pairs[cur * other] += 1
            singles.add(cur)
        res = 0
        for val in pairs.values():
            if val<2:
                continue
            res += val * (val - 1) // 2
        return res<<3

    main = tupleSameProduct


TESTS = [
    (
        ([1, 2, 3, 6],),
        8
    )
    ,
    (
        ([1, 2, 3],),
        0
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
