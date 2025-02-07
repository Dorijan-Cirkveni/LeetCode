from typing import *


class Solution:
    def __init__(self):
        self.dist = None
        self.by_index = None
        self.by_color = None

    def query(self, ind, color):
        cur_color=self.by_index.get(ind,0)
        if cur_color==color:
            return
        if cur_color:
            left=self.by_color[cur_color]
            left.remove(ind)
            if not left:
                self.by_color.pop(cur_color)
                self.dist-=1
        self.by_index[ind]=color
        if color not in self.by_color:
            self.dist+=1
            self.by_color[color]=set()
        self.by_color[color].add(ind)
        return
    def queryResults(self, _limit: int, queries: List[List[int]]) -> List[int]:
        self.by_color={}
        self.by_index={}
        self.dist=0
        queries.reverse()
        res=[]
        while queries:
            cur=queries.pop()
            self.query(*cur)
            res.append(self.dist)
        return res

    main = queryResults


TESTS = [
    (
        (4, [[0,1],[1,2],[2,2],[3,4],[4,5]]),
        [1,2,2,3,4]
    )
    ,
    (
        (4, [[1,4],[2,5],[1,3],[3,4]]),
        [1,2,2,3]
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
