import bisect
from typing import *


class Solution(object):
    def __init__(self):
        self.k = 0
        self.nums = []

    def checkCap(self, cap:int):
        steal = 0
        last_stolen = False
        for e in self.nums:
            if last_stolen:
                last_stolen = False
                continue
            if e > cap:
                continue
            steal += 1
            if steal == self.k:
                return True
            last_stolen = True
        return False

    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = nums
        self.k = k
        x0 = xM = nums[0]
        for e in nums:
            if e < x0:
                x0 = e
            elif e > xM:
                xM = e
        ran = range(x0,xM)
        res_ind = bisect.bisect_left(ran, 1, key=self.checkCap)
        res = x0 + res_ind
        return res

    main = minCapability


TESTS = [
    (
        ([2, 3, 5, 9], 2),
        5
    )
    ,
    (
        ([2, 7, 9, 3, 1], 2),
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
