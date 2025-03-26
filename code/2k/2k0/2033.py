from collections import defaultdict
from typing import *


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total=len(grid)*len(grid[0])
        offset=grid[0][0]%x
        counts=defaultdict(int)
        for e in grid:
            for f in e:
                counts[f-offset]+=1
        grid=None
        _grid=grid
        for e in counts:
            if e%x:
                return -1
        counts=[(e//x,v) for e,v in counts.items()]
        counts.sort()
        i=-1
        while total>0:
            i+=1
            new_total=total-counts[i][1]*2
            if -new_total>total:
                break
            total=new_total
        res=0
        avg=counts[i][0]
        for e,v in counts:
            res+=abs(e-avg)*v
        counts=None
        _counts=counts
        return res





    main =  minOperations


TESTS = [
    (([[529,529,989],[989,529,345],[989,805,69]],92),25),
    (
        ([[2,4,6,8]],2),
        4
    )
    ,
    (
        ([[1,5,2,3]],1),
        5
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
