from typing import *


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        incounts = [0] * len(favorite)
        for e in favorite:
            incounts[e] += 1
        nexstack = [i for i, e in enumerate(incounts) if not e]
        visited = [False] * len(favorite)
        lens = {}
        while nexstack:
            cur = nexstack.pop()
            visited[cur] = True
            size = lens.get(cur, 0)
            size += 1
            cur = favorite[cur]
            incounts[cur] -= 1
            lens[cur] = max(lens.get(cur, 0), size)
            if not incounts[cur]:
                nexstack.append(cur)
        maxcycle = 0
        totalchains = 0
        for i, e in enumerate(favorite):
            if visited[i]:
                continue
            count = 1
            visited[i] = True
            while not visited[e]:
                visited[e] = True
                count += 1
                e = favorite[e]
            if count == 2:
                e = favorite[e]
                totalchains += 2 + lens.pop(i,0) + lens.pop(e,0)
            elif maxcycle < count:
                maxcycle = count
        return max(maxcycle, totalchains)

    main = maximumInvitations


TESTS = [
    (
        ([3, 0, 1, 4, 1],),
        4
    )
    ,
    (
        ([1, 0, 3, 2, 5, 6, 7, 4, 9, 8, 11, 10, 11, 12, 10],),
        11
    )
    ,
    (
        ([2, 2, 1, 2],),
        3
    )
    ,
    (
        ([1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8],),
        6
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
