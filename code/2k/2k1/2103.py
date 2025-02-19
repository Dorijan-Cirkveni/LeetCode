from typing import *
import inspect


class Solution:
    def countPoints(self, rings: str) -> int:
        all_rods=0
        for i in range(0,len(rings),2):
            col='RGB'.index(rings[i])
            col+=int(rings[i+1])*3
            all_rods|=1<<col
        res=0
        for i in range(10):
            res+=int(all_rods&7==7)
            all_rods>>=3
        return res

    main = countPoints


TESTS = [
    (
        ([0, 1], 1),
        "test")
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
