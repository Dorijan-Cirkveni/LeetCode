from typing import *


def comp(s1, s2):
    diff = 0
    for a, b in zip(s1, s2):
        diff += a != b
    return diff


def addWordToGroup(G, wordList: list, i, e):
    curset = set()
    for j in range(i):
        if comp(wordList[j], e) == 1:
            curset.add(j)
            G[j].add(i)
    G.append(curset)


def groupWords(wordList: List[str], specials: dict):
    G: list[set[int]] = []
    for i, e in enumerate(wordList):
        if e in specials:
            specials[e] = i
        addWordToGroup(G, wordList, i, e)
    return G


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        specials = {beginWord: -1, endWord: -1}
        G = groupWords(wordList, specials)
        if specials[endWord] == -1:
            return []
        if specials[beginWord] == -1:
            specials[beginWord] = len(wordList)
            wordList.append(beginWord)
            addWordToGroup(G, wordList, specials[beginWord], beginWord)
        curset = {}
        used: set[int] = set()
        curset[specials[endWord]] = [[]]
        while curset and specials[beginWord] not in curset:
            nexset = {}
            used |= set(curset)
            for e, L in curset.items():
                nexvals = G[e] - used
                for nexval in nexvals:
                    L2 = nexset.setdefault(nexval, [])
                    for prevals in L:
                        curvals = prevals + [e]
                        L2.append(curvals)
            curset = nexset
        M = curset.pop(specials[beginWord],[])
        curset.clear()
        RES = []
        while M:
            L = M.pop()
            L2 = [beginWord]
            while L:
                i = L.pop()
                e = wordList[i]
                L2.append(e)
            RES.append(L2)
        return RES

    main = findLadders


TESTS = [
    (
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        5
    )
    ,
    (
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
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
