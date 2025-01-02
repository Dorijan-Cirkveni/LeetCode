from typing import *
import inspect


def makeOccurenceList(s):
    occurrences={e:[] for e in s}
    for i,e in enumerate(s):
        occurrences[e].append(i)
    return occurrences
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        occ=makeOccurenceList(s)
        valid=[e for e in occ if len(occ[e])>=k]
        valid.sort(key=lambda e:occ[e][0])


    main = longestSubsequenceRepeatedK


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
