from typing import *
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = {}
        while words2:
            word = words2.pop()
            cur = list(Counter(word).items())
            while cur:
                e, v = cur.pop()
                last = universal.get(e, 0)
                if last < v:
                    universal[e] = v
        res = []
        while words1:
            word = words1.pop()
            cur = Counter(word)
            for e, v in universal.items():
                if cur.get(e, 0) < v:
                    break
            else:
                res.append(word)
        return res

    main = wordSubsets


TESTS = [
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]),
        ["facebook", "google", "leetcode"]
    )
    ,
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]),
        ["apple", "google", "leetcode"]
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
        true_res.reverse()
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
