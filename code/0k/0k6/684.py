from typing import *

class DynamicGroup:
    def __init__(self):
        self.lead={}

    def flatten(self,cur):
        if cur not in self.lead:
            return cur
        nex=self.lead[cur]
        while nex in self.lead:
            self.lead[cur]=nex
            nex=self.lead[nex]
        return nex

    def check(self,a,b):
        return self.flatten(a)==self.flatten(b)

    def join(self,a,b):
        la=self.flatten(a)
        lb=self.flatten(b)
        self.lead[b]=la
        self.lead[lb]=la


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dgl=DynamicGroup()
        edges.reverse()
        while edges:
            el=edges.pop()
            if dgl.check(*el):
                return el
            dgl.join(*el)
        return [-1,-1]
    main = findRedundantConnection


TESTS = [
    (
        ([[1,2],[1,3],[2,3]], ),
        [2,3]
    )
    ,
    (
        ([[1,2],[2,3],[3,4],[1,4],[1,5]],),
        [1,4]
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
