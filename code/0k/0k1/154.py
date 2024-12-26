from typing import *
import inspect


def checkSegment(segments: list, a: int, b: int):
    if b - a > 1:
        segments.append((a, b))


class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums) - 1
        if nums[a] < nums[b]:
            return nums[0]
        segments = [(a, b)]
        while segments:
            a, b = segments.pop()
            c = (a + b) >> 1
            if nums[a] > nums[c]:
                b = c
                break
            if nums[c] > nums[b]:
                a = c
                break
            checkSegment(segments, a, c)
            checkSegment(segments, c, b)
        else:
            return nums[0]
        segments.clear()
        while b - a > 1:
            c = (a + b) // 2
            if nums[c] > nums[b]:
                a = c
            else:
                b = c
        return nums[b]

    main = findMin


TESTS = [
    (
        ([1, 3, 5],),
        1
    )
    ,
    (
        ([2, 2, 2, 0, 1],),
        0
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
