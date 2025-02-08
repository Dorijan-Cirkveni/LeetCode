import heapq
from typing import *


class NumberContainers:

    def __init__(self):
        self.numbers: dict[int, int] = dict()
        self.indices: dict[int, list] = dict()

    def popUsed(self, number):
        used = self.indices.get(number, [])
        while used and self.numbers[used[0]] != number:
            heapq.heappop(used)
        if not used:
            self.indices.pop(number,[])

    def change(self, index: int, number: int) -> None:
        old = 0
        if index in self.numbers:
            old = self.numbers[index]
        if old == number:
            return
        self.numbers[index] = number
        new_list = self.indices.setdefault(number, [])
        heapq.heappush(new_list, index)
        if old:
            self.popUsed(old)

    def find(self, number: int) -> int:
        return self.indices.get(number, [-1])[0]


null = None
MAINCLASS = NumberContainers


def testfn(functions: list[str], args: list[list]):
    functions.reverse()
    args.reverse()
    functions.pop()
    _c_args = args.pop()
    cls: MAINCLASS = MAINCLASS()
    res = [None]
    while functions:
        c_fn = functions.pop()
        fn = MAINCLASS.__getattribute__(cls, c_fn)
        c_args = args.pop()
        cures = fn(*c_args)
        res.append(cures)
    return res


TESTS = [
    (
        ["NumberContainers","find","change","change","change","change","find","change","find"],
        [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]],
        [null,-1,null,null,null,null,1,null,2]
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    count = 0
    print("Running...")
    for i, (functions, args, true_res) in enumerate(tests):
        res = testfn(functions, args)
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
