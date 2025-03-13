from typing import *


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        

    main = minZeroArray


TESTS = [
    (
        ([2,0,0,8,6],[[0,1,2],[0,3,1],[4,4,2],[0,1,2],[3,3,4],[2,3,1],[0,4,2],[3,4,3],[4,4,5],[0,4,3],[0,3,2],[0,3,1],[2,3,4],[3,4,3],[3,4,5]]),8
    )
    ,
    (
        ([7,6,8],[[0,0,2],[0,1,5],[2,2,5],[0,2,4]]),4
    )
    ,
    (
        ([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]),
        2
    ),
    (
        ([500000]*500000,[[0,500000-1,5]]*100000),
        100000
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
