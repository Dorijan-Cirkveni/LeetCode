import heapq
from heapq import heappush, heappop
from typing import *
import inspect


def incrementValueNeg(a, b):
    nex = a + 1.0
    nex /= b + 1
    nex -= a / b
    return -nex, a, b


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        class_heap = []
        while classes:
            a, b = classes.pop()
            E = incrementValueNeg(a, b)
            heapq.heappush(class_heap, E)
        while extraStudents:
            extraStudents -= 1
            c, a, b = heappop(class_heap)
            a += 1
            b += 1
            E = incrementValueNeg(a, b)
            heappush(class_heap, E)
        res=0.0
        size=0
        while class_heap:
            _,a,b=class_heap.pop()
            res+=a/b
            size+=1
        return res/size

    main = maxAverageRatio


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
