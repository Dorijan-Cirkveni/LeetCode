from typing import *


def reverseGraph(graph: List[List[int]], new_graph: List[Set[int]]) -> dict[int, set[int]]:
    origins = {}
    cur = -1
    graph.reverse()
    while graph:
        cur += 1
        curlist = graph.pop()
        curset = set(curlist)
        new_graph.append(curset)
        while curlist:
            nex = curlist.pop()
            origins.setdefault(nex, list()).append(cur)
    return origins


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = [i for i, e in enumerate(graph) if not e]
        new_graph: List[set[int]] = []
        origins: dict = reverseGraph(graph, new_graph)
        graph = new_graph
        res = []
        while terminal:
            cur = terminal.pop()
            res.append(cur)
            prev_list = origins.pop(cur, [])
            for prev in prev_list:
                curset = graph[prev]
                curset.remove(cur)
                if curset:
                    continue
                terminal.append(prev)
        res.sort()
        return res

    main = eventualSafeNodes


TESTS = [
    (
        ([[1, 2], [2, 3], [5], [0], [5], [], []],),
        [2, 4, 5, 6]
    )
    ,
    (
        ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []],),
        [4]
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
