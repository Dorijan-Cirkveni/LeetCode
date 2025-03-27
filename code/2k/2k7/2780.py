import collections
from typing import *


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        nh=len(nums)//2
        for e,v in count:
            if v>nh:
                dominant=e
                break
        else:
            return -1
        left,right=0,count[dominant]
        n=len(nums)
        for i,e in enumerate(nums):
            if e==dominant:
                left+=1
                right-=1
            if left>i//2 and right>(n-i)//2:
                return i
        return -1


    main = minimumIndex


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
