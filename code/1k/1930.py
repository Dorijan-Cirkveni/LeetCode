import bisect
from typing import *
import inspect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        occurences = {e: [] for e in s}
        for i, e in enumerate(s):
            occurences[e].append(i)
        sequence = list(occurences)
        sequence.sort(key=lambda e: occurences[e][0])
        last = {e: 0 for e in occurences}
        res = 0
        for first in sequence:
            L = occurences[first]
            if len(L) == 1:
                continue
            f_start = L[0]
            f_end = L[-1]
            for mid in occurences:
                L2 = occurences[mid]
                if mid==first:
                    res+=len(L)>2
                    continue
                m_start = bisect.bisect_right(L2, f_start, last[mid])
                m_end = bisect.bisect_left(L2, f_end, m_start)
                last[mid] = m_start
                res += m_end != m_start
        return res

    main = countPalindromicSubsequence


TESTS = [
    (
        ("aabca",),
        3
    )
    ,
    (
        ("adc",),
        0
    )
    ,
    (
        ("bbcbaba",),
        4
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
