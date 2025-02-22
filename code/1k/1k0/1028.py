from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def parseRaw(traversal: str):
    level = 0
    curnum = ""
    res = []
    traversal += '-'
    for e in traversal:
        if e != '-':
            curnum += e
            continue
        if not curnum:
            level += 1
            continue
        cur = level, int(curnum)
        res.append(cur)
        level, curnum = 1, ""
    return res


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        actual_traversal = parseRaw(traversal)
        actual_traversal.reverse()
        num = actual_traversal.pop()[1]
        node_stack = [TreeNode(num)]
        while actual_traversal:
            level, num = actual_traversal.pop()
            new_node = TreeNode(num)
            if level >= len(node_stack):
                if node_stack:
                    node_stack[-1].left = new_node
                node_stack.append(new_node)
                continue
            while level < len(node_stack):
                node_stack.pop()
            node_stack[-1].right = new_node
            node_stack.append(new_node)
        return node_stack[0]

    main = recoverFromPreorder


TESTS = [
    (
        ("1-2--3--4-5--6--7",),
        None
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
