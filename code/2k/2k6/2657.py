from collections import defaultdict
from typing import *


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A.reverse()
        B.reverse()
        diff = defaultdict(int)
        acc = 0
        result = []
        while A:
            temp = A.pop()
            if diff[temp] < 0:
                acc += 1
            diff[temp] += 1
            temp = B.pop()
            if diff[temp] > 0:
                acc += 1
            diff[temp] -= 1
            result.append(acc)
        return result

    main = findThePrefixCommonArray


TESTS = [
    (
        ([1, 3, 2, 4], [3, 1, 2, 4]),
        [0, 2, 3, 4]
    )
    ,
    (
        ([2, 3, 1], [3, 1, 2]),
        [0, 1, 3]
    )
    ,
    (
        ([1, 1, 1], [1, 1, 1]),
        [1, 2, 3]
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
