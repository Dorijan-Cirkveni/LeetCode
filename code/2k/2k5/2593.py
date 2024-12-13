from typing import *
import inspect


class Solution:
    def findScore(self, nums: List[int]) -> int:
        for i,e in enumerate(nums):
            nums[i]=(e,i)
        nums.sort(reverse=True)
        marked=set()
        score=0
        while nums:
            e,i=nums.pop()
            if i in marked:
                continue
            score+=e
            marked|={i-1,i+1}
        return score

    main = findScore


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
