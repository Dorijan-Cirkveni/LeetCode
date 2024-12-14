from collections import deque, defaultdict
from typing import *
import inspect


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        low = nums[-1]
        high = low
        first_of = {}
        res = 0
        for left in range(len(nums) - 1, -1, -1):
            cur = nums[left]
            first_of[cur] = left
            if cur < low:
                low = cur
            elif cur > high:
                high = cur
            else:
                res += len(nums) - left
                continue
            if high - low > 5:
                low=high=cur
                first_of=defaultdict()
                while len(nums)>left:
                    nums.pop()
            while high - low > 2:
                cur = nums.pop()
                if first_of[cur] != len(nums):
                    continue
                first_of.pop(cur)
                while low not in first_of:
                    low += 1
                while high not in first_of:
                    high -= 1
            res += len(nums) - left
        return res

    main = continuousSubarrays


TESTS = [
    (
        ([5, 4, 2, 4],),
        8
    )
    ,
    (
        ([65, 66, 67, 66, 66, 65, 64, 65, 65, 64],),
        43
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
