from typing import *
import inspect


class Solution:
    def __init__(self):
        self.highest = None

    def setup(self, heights: List[int]):
        self.highest = []
        while len(heights) > 1:
            nexhei = []
            last = None
            for cur in heights:
                if last is None:
                    last = cur
                    continue
                if last < cur:
                    last = cur
                nexhei.append(last)
                last = None
            if last:
                nexhei.append(last)
            self.highest.append(heights)
            heights = nexhei
        for E in self.highest:
            E.append(-1)
        return

    def getHigherAfter(self, first, height):
        for i, heights in enumerate(self.highest):
            hei=heights[first+1]
            if hei > height:
                break
            elif hei == -1:
                return -1
            first >>= 1
        else:
            return -1
        first+=1
        while i > 0:
            i -= 1
            first <<= 1
            if self.highest[i][first] <= height:
                first |= 1
        return first

    def processQueries(self, heights: List[int], queries: List[List[int]]):
        best = max(heights)
        for first, second in queries:
            if first > second:
                first, second = second, first
            if first == second or heights[first] < heights[second]:
                yield second
                continue
            if second == len(heights) - 1 or heights[first] == best:
                yield -1
                continue
            yield self.getHigherAfter(second, heights[first])
        return

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        self.setup(heights)
        PQ = self.processQueries(heights, queries)
        RES = list(PQ)
        return RES

    main = leftmostBuildingQueries


TESTS = [
    (
        (
            [3,4,1,2],
            [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
        ),
        [0, 1, -1, -1, 1, 1, -1, -1, -1, -1, 2, 3, -1, -1, 3, 3]
    )
    ,
    (
        (
            [3,1,2,4],
            [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
        ),
        [0,3,3,3,3,1,2,3,3,2,2,3,3,3,3,3]
    )
    ,
    (
        (
            [1,4,2,3,5],
            [[1, 2]]
        ),
        [4]
    )
    ,
    (
        (
            [6, 4, 8, 5, 2, 7],
            [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
        ),
        [2, 5, -1, 5, 2]
    )
    ,
    (
        (
            [5, 3, 8, 2, 6, 1, 4, 6],
            [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
        ),
        [7, 6, -1, 4, 6]
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
