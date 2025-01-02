import bisect
from typing import *

class StockSpanner:

    def __init__(self):
        self.day=0
        self.past_monotonic=[(-float('inf'),0)]

    def use_queue(self,price):
        price=-price
        while self.past_monotonic[-1][0]>=price:
            self.past_monotonic.pop()
        self.past_monotonic.append((price,self.day))

    def next(self, price: int) -> int:
        self.day+=1
        self.use_queue(price)
        return self.day-self.past_monotonic[-2][-1]


null=None
MAINCLASS=StockSpanner

def testfn(functions:list[str],args:list[list]):
    functions.reverse()
    args.reverse()
    functions.pop()
    c_args=args.pop()
    cls:MAINCLASS=MAINCLASS(*c_args)
    res=[null]
    while functions:
        c_fn=functions.pop()
        fn=MAINCLASS.__getattribute__(cls,c_fn)
        c_args=args.pop()
        cures=fn(*c_args)
        res.append(cures)
    return res

TESTS = [
    (
        ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
        [[], [100], [80], [60], [70], [60], [75], [85]],
        [null, 1, 1, 1, 2, 1, 4, 6]
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
