from typing import *


class Solution:
    def atLeastCount(self, word: str, k: int) -> int:
        n = len(word)
        consonants = 0
        vows = {e: 0 for e in "aeiou"}
        vow_check = 5
        res = 0
        first = 0
        for last, c in enumerate(word):
            if c in vows:
                if vows[c] == 0:
                    vow_check -= 1
                vows[c] += 1
            else:
                consonants += 1
            while vow_check == 0 and consonants >= k:
                res += n-last
                c2 = word[first]
                first += 1
                if c2 not in vows:
                    consonants -= 1
                    continue
                vows[c2] -= 1
                if vows[c2] == 0:
                    vow_check += 1
        return res

    def countOfSubstrings(self, word: str, k: int) -> int:
        res = self.atLeastCount(word, k)
        res -= self.atLeastCount(word, k + 1)
        return res

    main = countOfSubstrings


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
