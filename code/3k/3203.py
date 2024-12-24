from collections import deque
from typing import *
import inspect


def MakeGraph(edges: List[List[int]]):
    n = len(edges) + 1
    ran = range(n)
    graph: list[set] = [set() for i in ran]
    while edges:
        a, b = edges.pop()
        graph[a].add(b)
        graph[b].add(a)
    return graph


def GetDiameterAndMinDistance(graph: list[set[int]]):
    leaves = deque([i for i, e in enumerate(graph) if len(e) == 1])
    data = {}
    dist, diam = 0, 0
    while leaves:
        curind = leaves.popleft()
        curset = graph[curind]
        dist, diam = data.pop(curind, (0, 0))
        dist += 1
        if not curset:
            continue
        nexind = curset.pop()
        nexset = graph[nexind]
        nexset.remove(curind)

        nex_dis, nex_diam = data.get(nexind, (0, 0))
        nex_diam = max(nex_diam, nex_dis + dist, diam)
        nex_dis = max(nex_dis, dist)
        data[nexind] = nex_dis, nex_diam

        if len(nexset) == 1:
            leaves.append(nexind)
    return dist, diam


def GetDiameterAndMinDistanceFromEdges(edges: List[List[int]]):
    if not edges:
        return 1,0
    graph = MakeGraph(edges)
    res = GetDiameterAndMinDistance(graph)
    return res


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        dist1, diam1 = GetDiameterAndMinDistanceFromEdges(edges1)
        dist2, diam2 = GetDiameterAndMinDistanceFromEdges(edges2)
        diam3 = dist1 + dist2 - 1
        return max(diam1, diam2, diam3)

    main = minimumDiameterAfterMerge


TESTS = [
    (
        (
            [],
            []
        ),
        1
    )
    ,
    (
        (
            [[0, 1], [0, 2], [0, 3]],
            [[0, 1]]
        ),
        3
    )
    ,
    (
        (
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
        ),
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
