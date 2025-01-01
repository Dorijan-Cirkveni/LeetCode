import math
from typing import *
import inspect


def numToNewBitCounter(n):
    L = []
    while n:
        n, b = divmod(n, 2)
        L.append(b)
    return L


def numToOldBitCounter(n, L):
    i = 0
    while n:
        n, b = divmod(n, 2)
        L[i] += b
        i += 1


def shaveCounter(L, k):
    res = 0
    for i, e in enumerate(L):
        if not e:
            continue
        L[i] -= k
        res |= 1 << i
    return res


def oldBitCounterToSquareSum(L,lim:int):
    A = list(set(L))
    A.sort(reverse=True)
    last = 0
    res = 0
    while A and lim:
        while not L[-1]:
            L.pop()
        cur = A.pop()
        delta = cur - last
        if delta>lim:
            delta=lim
        last = cur
        n = shaveCounter(L, delta)
        sqr=n*n*delta
        res += sqr
        lim-=delta
    return res


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        counts = numToNewBitCounter(nums.pop())
        while nums:
            numToOldBitCounter(nums.pop(), counts)
        res = oldBitCounterToSquareSum(counts,k)
        return res%(10**9+7)

    main = maxSum


TESTS = [
    (
        ([2,6,5,8], 2),
        261
    )
    ,
    (
        ([4,5,4,7], 3),
        90
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
