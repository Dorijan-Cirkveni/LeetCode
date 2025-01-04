from typing import *
import inspect
from collections import Counter, deque


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        diff = len(target) - len(words[0])
        if diff > 0:
            return 0
        target += '@'
        curlist = [0] * -diff
        curlist.append(1)
        for i, E in enumerate(zip(*words)):
            E: list
            freq = Counter(E)
            nexlist = []
            for ind, count in enumerate(curlist):
                if not count:
                    nexlist.append(0)
                    continue
                ind += diff
                char = target[ind]
                curcount = freq.get(char, 0)
                nexlist.append(count * curcount % (10 ** 9 + 7))
            for i in range(len(curlist) - 1):
                nexlist[i] += curlist[i + 1]
            curlist = nexlist
            while not curlist[-1]:
                curlist.pop()
                if not curlist:
                    return 0
            diff += 1
        return curlist[0] % (10 ** 9 + 7)

    main = numWays


TESTS = [
    (
        (['abba', 'baab'], 'babbbb'),
        0
    )
    ,
    (
        (["acca", "bbbb", "caca"], 'aba'),
        6
    )
    ,
    (
        (["abba", "baab"], 'bab'),
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
