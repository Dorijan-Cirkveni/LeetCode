from collections import deque
from typing import *
import inspect



class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        k<<=1
        nums.sort()
        nums.append(nums[-1]+k)
        first=0
        best=0
        for last,val in enumerate(nums):
            best=max(best,last-first)
            while val-nums[first]>k:
                first+=1
        return best
    main = maximumBeauty


TESTS = [
    (
        ([4,6,1,2], 2),
        3
    )
    ,
    (
        ([0, -1, 2, 3, 9], 2),
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
