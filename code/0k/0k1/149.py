import math
from typing import *


class Sequence:
    def __init__(self, anchor: tuple[int,int], vector: tuple[int,int], elements: set[int]):
        self.anchor = anchor
        self.vector = vector
        self.elements = elements


def vecdiv(vector: tuple[int,int]):
    a,b=vector
    c=math.gcd(a,b)
    return a//c,b//c

def tdivmod(a,b):
    c1,d1=divmod(a[0],b[0])
    c2,d2=divmod(a[1],b[1])
    return (c1,c2),(d1,d2)

def vecsub(a:tuple,b:tuple):
    return a[0]-b[0],a[1]-b[1]


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        sortedpoints: List[tuple] = []
        while points:
            rawel = points.pop()
            el = tuple(rawel)
            sortedpoints.append(el)
        sortedpoints.sort(reverse=True)
        res = 2
        firsts = []
        seqs: list[Sequence] = []
        curind = -1
        while sortedpoints:
            cur: tuple = sortedpoints.pop()
            curind += 1
            used = set()
            for seq in seqs:
                diff = seq.elements - used
                if not diff:
                    continue
                delta = vecsub(cur,seq.anchor)
                vector = seq.vector

                if 0 in vector:
                    ind = int(vector[0] != 0)
                    if delta[ind] != 0:
                        continue
                else:
                    delta, check = tdivmod(delta, vector)
                    if check!=(0,0):
                        continue
                    if delta[0] != delta[1]:
                        continue
                used |= diff
                seq.elements.add(curind)
                res = max(res, len(seq.elements))
            for i, vec in enumerate(firsts):
                if i in used:
                    used.remove(i)
                    continue
                delta = vecdiv(vecsub(cur,vec))
                newseq = Sequence(vec, delta, {i, curind})
                seqs.append(newseq)
            firsts.append(cur)
        return res

    main = maxPoints


TESTS = [
    (
        ([[2,3],[3,3],[-5,3]],),
        3
    )
    ,
    (
        ([[1, 1], [2, 2], [3, 3]],),
        3
    )
    ,
    (
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],),
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
