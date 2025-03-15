from typing import *


class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minimums = [[0, 0]]
        minimums[0][False] = 0
        for house in nums:
            n = len(minimums) - 1
            if n < k:
                minimums.append([float("inf")] * 2)
                n += 1
            cur_count = minimums[-1]
            for i in range(n, -1, -1):
                last_count = minimums[i]
                steal = max(min(cur_count[False], last_count[False]), house)
                if last_count[False] > last_count[True]:
                    last_count[False] = last_count[True]
                cur_count[True] = steal
                cur_count = last_count
        return min(minimums[-1])

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
