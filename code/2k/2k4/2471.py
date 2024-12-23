from typing import *
import inspect


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_swaps(layer:list[TreeNode]):
    n=len(layer)
    indices=[i for i in range(n)]
    indices.sort(key=lambda i:layer[i].val)
    print(indices)
    res=0
    for i in range(n):
        if indices[i]==i:
            continue
        res-=1
        while indices[i]!=i:
            j=indices[i]
            indices[i]=i
            i=j
            res+=1
    return res

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        curlist = [root]
        res=0
        while curlist:
            nex_list=[]
            res+=count_swaps(curlist)
            for el in curlist:
                nex_list+=[el.left,el.right]
            curlist=list(filter(bool,nex_list))
        return res

    main = minimumOperations


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
