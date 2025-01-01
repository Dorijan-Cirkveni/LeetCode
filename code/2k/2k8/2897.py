from typing import *
import inspect


def numToNewBitCounter(n):
    L=[]
    while n:
        n,b=divmod(n,2)
        L.append(n)
    return L
def numToOldBitCounter(n,L):
    i=0
    n,b=divmod(n,2)
    L[i]+=b
    i+=1
def oldBitCounterToCurnum(L):
    A=L[:]
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        counts=numToNewBitCounter(nums.pop())
        while nums:
            numToOldBitCounter(nums.pop(),counts)

    main = maxSum


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
