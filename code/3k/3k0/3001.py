from typing import *
import inspect


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a==e:
            if a!=c:
                return 1
            if (d-b)*(d-f)>0:
                return 1
        elif b==f:
            if b!=d:
                return 1
            if (c-a)*(c-e)>0:
                return 1
        if c+d==e+f:
            if c+d!=a+b:
                return 1
            if (a-c)*(a-e)>0:
                return 1
        elif c-d==e-f:
            if c-d!=a-b:
                return 1
            if (a-c)*(a-e)>0:
                return 1
        return 2

    main = minMovesToCaptureTheQueen


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
