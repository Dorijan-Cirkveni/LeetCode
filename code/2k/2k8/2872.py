from collections import defaultdict, deque
from typing import *
import inspect


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if not edges:
            return 1
        X = [set() for _ in range(n)]
        while edges:
            a, b = edges.pop()
            X[a].add(b)
            X[b].add(a)
        cur_leaves = deque([i for i, e in enumerate(X) if len(e) == 1])
        res = 1
        while n > 1:
            n -= 1
            cur = cur_leaves.popleft()
            val = values[cur] % k
            if val == 0:
                res += 1
            nex = X[cur].pop()
            X[nex].remove(cur)
            values[nex] += val
            values[nex] %= k
            if len(X[nex]) == 1:
                cur_leaves.append(nex)
        return res

    main = maxKDivisibleComponents


TESTS = [
    (
        (
            2,
            [[1, 0]],
            [0, 0],
            99
        ),
        2
    )
    ,
    (
        (
            5,
            [[0, 2], [1, 2], [1, 3], [2, 4]],
            [1, 8, 1, 4, 4],
            6
        ),
        2
    )
    ,
    (
        (
            7,
            [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
            [3, 0, 6, 1, 5, 2, 1],
            3
        ),
        3
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
