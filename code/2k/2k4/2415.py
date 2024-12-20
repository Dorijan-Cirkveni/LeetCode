from typing import *
import inspect


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

is_not_none=lambda el: el is not None
def getNext(cur:list[TreeNode]):
    res=[]
    for el in cur:
        ls=el.left,el.right
        fil=filter(is_not_none,ls)
    return res


def reverse_vals(cur:list[TreeNode]):
    for i in range(len(cur)//2):
        a=cur[i]
        b=cur[~i]
        temp=a.val
        a.val=b.val
        b.val=temp


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        cur=[root]
        while cur:
            cur=getNext(cur)
            reverse_vals(cur)
            cur=getNext(cur)
        return root


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
