from typing import *


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if not num2:
            return 0
        num2 = num2.bit_count()
        if num2 >= num1.bit_length():
            return (1 << num2) - 1
        ref = num1.bit_count()
        if num2 <= ref:
            for _ in range(ref - num2):
                num1 &= num1 - 1
            return num1
        for _ in range(num2 - ref):
            num1 |= num1 + 1
        return num1

    main = minimizeXor


TESTS = [
    ((10,7),11),

    ((1,0),0),
    ((2,1),2),
    ((1,1),1),
    ((1,11),7),
    ((10,1),8),
    ((10,3),10),
    ((10,15),15),
    ((0,0),0)
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
