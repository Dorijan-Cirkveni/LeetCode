import heapq
from collections import defaultdict
from typing import *
import inspect


def groupString(s):
    cur = s[0]
    first = 0
    s += '@'
    res = []
    for i, e in enumerate(s):
        if e != cur:
            el = cur, i - first
            res.append(el)
            first = i
            cur = e
    return res


def groupByChar(specials: list) -> dict[any, list[int]]:
    by_char: dict[any, list[int]] = {c: [0]*3 for c, _ in specials}
    while specials:
        c, n = specials.pop()
        best=by_char[c]
        for i in range(n, n - 3, -1):
            if best[0] >= i:
                break
            heapq.heappush(best, i)
            heapq.heappop(best)
    return by_char


def evaluate(by_char: dict[any, list[int]]):
    res = 0
    for e in list(by_char):
        best = by_char.pop(e)
        res = max(res, best[0])
    return res-int(res==0)


class Solution:
    def maximumLength(self, s: str) -> int:
        specials = groupString(s)
        by_char = groupByChar(specials)
        res = evaluate(by_char)
        return res

    main = maximumLength


TESTS = [
    (
        ("aa",),
        -1)
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
