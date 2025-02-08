from typing import *


class BasicTrieNode:
    def __init__(self):
        self.indices: set = set()
        self.next = {}

    def add(self, c):
        nex = self.next.get(c, BasicTrieNode())
        self.next[c] = nex
        return nex

    def check(self, c, default=None):
        return self.next.get(c, default)

    def get_all(self):
        indices = set()
        stack = [self]
        while stack:
            cur = stack.pop()
            indices |= cur.indices
            vals = cur.next.values()
            stack += list(vals)
        return indices


class BasicTrie:
    def __init__(self):
        self.root = BasicTrieNode()

    def add(self, s, ind: int):
        cur: BasicTrieNode = self.root
        for e in s:
            cur = cur.add(e)
        cur.indices.add(ind)

    def step(self, L: List[BasicTrieNode], c):
        NL = []
        for el in L:
            nel = el.check(c)
            if nel is None:
                continue
            NL.append(nel)
        NL.append(self.root)
        return NL


class Solution:

    def __init__(self):
        self.start = None
        self.end = None

    def countBothSides(self, word: str, antiword: str):
        cur_start = self.start.root
        cur_end = self.end.root
        for a, b in zip(word, antiword):
            cur_start = cur_start.check(a)
            cur_end = cur_end.check(b)
            if cur_start is None or cur_end is None:
                return 0
        res = cur_start.get_all()
        if res:
            res &= cur_end.get_all()
        return len(res)

    def addBothSides(self, word: str, antiword: str, ind: int):
        self.start.add(word, ind)
        self.end.add(antiword, ind)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        self.start = BasicTrie()
        self.end = BasicTrie()
        i = -1
        res = 0
        while words:
            i += 1
            word = words.pop()
            antiword = word[::-1]
            res += self.countBothSides(word, antiword)
            if words:
                self.addBothSides(word, antiword, i)
        return res

    main = countPrefixSuffixPairs


TESTS = [
    (
        (["b", "ba", "b", "b", "b"],),
        6
    )
    ,
    (
        (["a", "aba", "ababa", "aa"],),
        4
    )
    ,
    (
        (["pa", "papa", "ma", "mama"],),
        2
    )
    ,
    (
        (["abab", "ab"],),
        0
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
