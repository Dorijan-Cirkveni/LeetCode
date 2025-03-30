from typing import *


class Solution:
    @staticmethod
    def getFirstAndLast(s: str) -> tuple[dict, dict]:
        beginnings = {}
        ends = {}
        for i, e in enumerate(s):
            beginnings.setdefault(e, i)
            ends[e] = i
        return beginnings, ends

    @staticmethod
    def getStack(s: str):
        begin, end = Solution.getFirstAndLast(s)
        stack = [(ind, False, char) for char, ind in begin.items()]
        stack += [(ind, True, char) for char, ind in end.items()]
        stack.sort(reverse=True)
        return stack

    @staticmethod
    def getRes(stack):
        res = []
        curfirst = 0
        used = set()
        while stack:
            ind, mode, char = stack.pop()
            if not mode:
                used.add(char)
                continue
            used.remove(char)
            if used:
                continue
            ind += 1
            res.append(ind - curfirst)
            curfirst = ind
        return res

    def partitionLabels(self, s: str) -> List[int]:
        stack = self.getStack(s)
        res = self.getRes(stack)
        return res

    main = partitionLabels


TESTS = [
    (
        ("ababcbacadefegdehijhklij",),
        [9,7,8]
    )
    ,
    (
        ("eccbbbbdec",),
        [10]
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
