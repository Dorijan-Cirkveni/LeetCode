from typing import *


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(locked) & 1 == 1:
            return False
        minval = 0
        maxval = 0
        for par, status in zip(s, locked):
            check = 0 if status == '0' else 1 if par == '(' else -1
            if check >= 0:
                maxval += 1
            else:
                maxval -= 1
            if check <= 0 and minval != 0:
                minval -= 1
            else:
                minval += 1
            if minval > maxval:
                return False
        return minval == 0

    main = canBeValid


TESTS = [
    (
        ("))()))", "010100"),
        True
    )
    ,
    (
        ("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
         "100011110110011011010111100111011101111110000101001101001111"),
        False
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
