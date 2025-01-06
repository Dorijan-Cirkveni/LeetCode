from typing import *
import inspect


def calculateThreshold(below: int, power: int):
    rem = (below >> power) + 1
    return rem << power


def calculateMask(power: int):
    return (1 << power) - 1


def groupBelow(nums: list[int], maxval: int):
    power = maxval.bit_length()
    mask = calculateMask(power)
    threshold = 0
    nums.sort(reverse=True)
    curgroup = []
    groups = []
    while nums:
        cur = nums.pop()
        if cur >= threshold:
            curgroup = []
            groups.append(curgroup)
            threshold = calculateThreshold(cur, power)
        curgroup.append(cur & mask)
    return groups


def countBelow(nums: int, maxval: int):
    nums.sort()


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        return -1

    main = countBelow


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
