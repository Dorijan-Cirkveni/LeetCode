from typing import *


class Solution:
    def __init__(self):
        self.parents = None

    def findRoot(self, node:int):
        while self.parents[node]!=node:
            self.parents[node]=node
            node=self.parents[node]
        return node
    def getRes(self, cost, a, b):
        if a==b:
            return 0
        ar=self.findRoot(a)
        br=self.findRoot(b)
        if ar!=br:
            return -1
        return cost[ar]

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        self.parents=list(range(n))
        cost=[-1]*n
        for a,b,v in edges:
            ar=self.findRoot(a)
            br=self.findRoot(b)
            cost[br]&=v
            if a!=b:
                cost[br]&=cost[ar]
                self.parents[ar]=br
        edges=None
        result=[self.getRes(cost,*e) for e in query]
        return result

    main = minimumCost


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
