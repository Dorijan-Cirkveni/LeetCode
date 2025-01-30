from typing import *


class UndirectedGraph:
    def __init__(self, links: dict = None):
        self.links = links if links else {}
        self.start=None

    def addLink(self, a, b):
        self.links.setdefault(a, set()).add(b)
        self.links.setdefault(b, set()).add(a)
        self.start=a

    def extractGraph(self,start):
        found={start}
        nex=[start]
        while nex:
            cur=nex.pop()
            curset=self.links[cur]-found
            found|=curset
            nex+=list(curset)
        return found

    def connectionSplit(self):
        graphs = []
        for e in list(self.links):
            if e not in self.links:
                continue
            curset=self.extractGraph(e)
            if len(curset)==len(self.links):
                self.start=e
                graphs.append(self)
                break
            links = {e: self.links.pop(e) for e in curset}
            graph = UndirectedGraph(links)
            graph.start=e
            graphs.append(graph)
        return graphs

    def chessCheck(self):
        white = {self.start}
        black = set()
        curset = white
        while curset:
            nexset = set()
            white |= curset
            for cur in curset:
                cur_nex = self.links[cur] - black
                if cur_nex & white:
                    return False
                nexset |= cur_nex
            curset = nexset
            black, white = white, black
        return True

    def furthestDistFrom(self, e):
        curset = {e}
        last_set = set()
        dist = -1
        while curset:
            dist += 1
            nexset = set()
            for e in curset:
                v = self.links[e] - last_set
                nexset |= v
            last_set = curset
            curset = nexset
        return dist, last_set

    def ends(self):
        return [e for e, v in self.links.items() if len(v) == 1]

    def bestStretch(self):
        ends = self.ends()
        if not ends:
            ends=[self.start]
        used = set(ends)
        best = 0
        while ends:
            cur = ends.pop()
            dist, curset = self.furthestDistFrom(cur)
            curset -= used
            used |= curset
            ends += list(curset)
            if best < dist:
                best = dist
        return best + 1


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        gr = UndirectedGraph()
        while edges:
            a, b = edges.pop()
            gr.addLink(a - 1, b - 1)
        n -= len(gr.links)
        graphs = gr.connectionSplit()
        res = 0
        for cur_gr in graphs:
            if not cur_gr.chessCheck():
                return -1
            res += cur_gr.bestStretch()
        return res + n

    main = magnificentSets


TESTS = [
    (
        (
            30,
[[1,9],[30,27],[21,9],[2,10],[16,28],[1,27],[20,24],[22,24],[30,6],[30,19],[1,19],[30,11],[16,6],[16,29],[2,29],[2,23],[16,24],[1,25],[1,17],[16,23],[30,26],[16,12],[1,14],[13,23],[13,14],[2,19],[22,6],[30,3],[30,18],[20,8],[13,24],[20,9],[20,14],[13,28],[13,10],[2,8],[16,7],[16,10],[21,5],[20,15],[20,11],[2,26],[21,3],[22,10],[16,8],[2,17]]
        ),
        -2
    )
    ,
    (
        (
            26,
            [[9, 16], [8, 3], [20, 21], [12, 16], [14, 3], [7, 21],
             [22, 3], [22, 18], [11, 16], [25, 4], [2, 4], [14, 21],
             [23, 3], [17, 3], [2, 16], [24, 16], [13, 4], [10, 21],
             [7, 4], [9, 18], [14, 18], [14, 4], [14, 16], [1, 3],
             [25, 18], [17, 4], [1, 16], [23, 4], [2, 21], [5, 16],
             [24, 18], [20, 18], [19, 16], [24, 21], [9, 3], [24, 3],
             [19, 18], [25, 16], [19, 21], [6, 3], [26, 18], [5, 21],
             [20, 16], [2, 3], [10, 18], [26, 16], [8, 4], [11, 21],
             [23, 16], [13, 16], [25, 3], [7, 18], [19, 3], [20, 4],
             [26, 3], [23, 18], [15, 18], [17, 18], [10, 16], [26, 21],
             [23, 21], [7, 16], [8, 18], [10, 4], [24, 4], [7, 3], [11, 18],
             [9, 4], [26, 4], [13, 21], [22, 16], [22, 21], [20, 3], [6, 18],
             [9, 21], [10, 3], [22, 4], [1, 18], [25, 21], [11, 4], [1, 21], [15, 3],
             [1, 4], [15, 16], [2, 18], [13, 3], [8, 21], [13, 18], [11, 3], [15, 21],
             [8, 16], [17, 16], [15, 4], [12, 3], [6, 4], [17, 21], [5, 18], [6, 16],
             [6, 21], [12, 4], [19, 4], [5, 3], [12, 21], [5, 4]]
        ), 4
    )
    ,
    (
        (6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]),
        4
    )
    ,
    (
        (3, [[1, 2], [2, 3], [3, 1]]),
        -1
    )
    ,
    (
        (4, [[1, 2], [3, 4]]),
        4
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
