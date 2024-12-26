import math
from typing import *
import inspect


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return '0'
        prefix=False
        if numerator<0:
            prefix=not prefix
            numerator=-numerator
        if denominator<0:
            prefix=not prefix
            denominator=-denominator
        divisor = math.gcd(numerator, denominator)
        numerator //= divisor
        denominator //= divisor
        integer, numerator = divmod(numerator, denominator)
        res = '-'*prefix+str(integer)
        if not numerator:
            return res
        res += '.'
        temp = ''
        occurences = {}
        i = 0
        while numerator not in occurences:
            occurences[numerator] = i
            i += 1
            integer, numerator = divmod(numerator * 10, denominator)
            temp += str(integer)
            if not numerator:
                res += temp
                break
        else:
            i = occurences[numerator]
            res += '{}({})'.format(temp[:i], temp[i:])
        return res

    main = fractionToDecimal


TESTS = [
    (
        (1, 2),
        "0.5"
    )
    ,
    (
        (1, 3),
        "0.(3)"
    )
    ,
    (
        (2, 14),
        "0.(142857)"
    )
    ,
    (
        (-50,8),
        "-6.25"
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
