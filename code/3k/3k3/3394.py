from typing import *


def splitRectangles(rectangles: List[List[int]])->tuple[List[tuple[int,int]],List[tuple[int,int]]]:
    rec_x=[]
    rec_y=[]
    for stx,sty,enx,eny in rectangles:
        crx=stx,enx
        cry=sty,eny
        rec_x.append(crx)
        rec_y.append(cry)
    return rec_x,rec_y
def groupUntilThreshold(ranges:List[tuple[int,int]],thr:int=3):
    last=0
    ranges.sort(key=lambda e:e[0])
    for start,end in ranges:
        if start>=last:
            thr-=1
            if not thr:
                return True
        if last<end:
            last=end
    return False
class Solution:
    def checkValidCuts(self, _n: int, rectangles: List[List[int]]) -> bool:
        if len(rectangles)<3:
            return False
        rec_x,rec_y=splitRectangles(rectangles)
        if groupUntilThreshold(rec_x):
            return True
        if groupUntilThreshold(rec_y):
            return True
        return False
    main = checkValidCuts


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
