import bisect
from typing import *
import inspect


class Solution:
    def __init__(self):
        self.k = None
        self.nums = None

    def step(self, last_list, offset):
        k = self.k
        new_list = []
        cursum = sum(self.nums[offset-k:offset])
        best_data=[]
        best = 0
        for i in range(offset,len(self.nums)):
            last, data=last_list[i-offset]
            cures = last + cursum
            if best<cures:
                best=cures
                best_data=data+[i-k]
            new_list.append((best,best_data))
            cursum += self.nums[i]
            cursum -= self.nums[i-k]
        return new_list

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        self.nums = nums
        nums.append(0)
        self.k = k
        best = [(0,[])]*len(nums)
        for i in range(1,4):
            best=self.step(best,i*k)
            print(best)
        ind = bisect.bisect_left(best,best[-1][0],key=lambda e:e[0])
        return best[ind][1]


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
