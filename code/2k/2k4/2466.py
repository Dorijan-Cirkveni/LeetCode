import heapq
from typing import *
import inspect

MOD = (10 ** 9) + 7


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        pq = [0]
        curset = {0: 1}
        res = 0
        while pq:
            cur = heapq.heappop(pq)
            val = curset.pop(cur)
            if cur >= low:
                res += val
                res %= MOD
            for delta in (zero, one):
                nex = cur + delta
                if nex > high:
                    continue
                if nex in curset:
                    curset[nex] += val
                    curset[nex] %= MOD
                else:
                    heapq.heappush(pq, nex)
                    curset[nex] = val
        return res % MOD

    main = countGoodStrings


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
