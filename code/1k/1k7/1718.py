from typing import *


class Solution:
    def __init__(self, n=1):
        self.n = n
        self.res = [0] * (2 * n - 1)
        self.curset = set()

    def solve(self, indx: int, count: int):
        if count + 1 == self.n << 1:
            return True
        indx = self.res.index(0, indx)
        lim = len(self.res) - indx - 1
        if lim > self.n:
            lim = self.n
        for i in range(lim, 1, -1):
            if i in self.curset:
                continue
            if self.res[indx + i]:
                continue
            self.curset.add(i)
            self.res[indx] = self.res[indx + i] = i
            if self.solve(indx + 1, count + 2):
                return True
            self.res[indx] = self.res[indx + i] = 0
            self.curset.remove(i)
        if 1 in self.curset:
            return False
        self.curset.add(1)
        self.res[indx] = 1
        if self.solve(indx + 1, count + 1):
            return True
        self.res[indx] = 0
        self.curset.remove(1)
        return False

    def constructDistancedSequence(self, n: int) -> List[int]:
        if not n:
            return []
        self.__init__(n)
        self.solve(0, 0)
        return self.res

    main = constructDistancedSequence


TESTS = [
    (
        (3,),
        [3, 1, 2, 3, 2]
    )
    ,
    (
        (20,),
        [20,18,19,15,13,17,10,16,7,5,3,14,12,3,5,7,10,13,15,18,20,19,17,16,12,14,11,9,4,6,8,2,4,2,1,6,9,11,8]
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
