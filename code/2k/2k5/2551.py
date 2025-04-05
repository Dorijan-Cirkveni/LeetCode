from typing import *


class Solution:
    def findStep(self, cur_best: List[int], reverse: bool):
        minmax = min if reverse else max
        last_best = float("inf") if reverse else float("-inf")
        nex_best = [last_best]
        for i, e in enumerate(self.weights):
            last_best = minmax(last_best, e + cur_best[i])
            nex_best.append(last_best + e)
        return nex_best

    def findBest(self, k: int, reverse: bool):
        last_best = float("inf") if reverse else float("-inf")
        cur_best = [0] + [last_best]*len(self.weights)
        for _ in range(k):
            cur_best = self.findStep(cur_best, reverse=reverse)
        return cur_best[-1]

    def putMarbles(self, weights: List[int], k: int) -> int:
        self.weights = weights
        minval = self.findBest(k, True)
        maxval = self.findBest(k, False)
        return maxval - minval

    main = putMarbles


TESTS = [
    (
        ([1,3,5,1], 2),
        4
    )
    ,
    (
        ([0, 1], 2),
        0
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
