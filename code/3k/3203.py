from typing import *
import inspect


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        return -1

    main = minimumDiameterAfterMerge


TESTS = [
    (
        (
            [[0,1],[0,2],[0,3]],
            [[0,1]]
        ),
        3
    )
    ,
    (
        (
            [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]],
            [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
        ),
        5
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
