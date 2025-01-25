from typing import *


def getSortedEnum(nums: list):
    cur = -1
    res = []
    nums.reverse()
    while nums:
        cur += 1
        val = nums.pop(), cur
        res.append(val)
    res.sort()
    return res


def separateByLimit(sorted_enum: list[tuple], limit: int):
    cur_g = [sorted_enum.pop()]
    groups = [cur_g]
    while sorted_enum:
        cur = sorted_enum.pop()
        diff = cur_g[-1][0] - cur[0]
        if diff > limit:
            cur_g = []
            groups.append(cur_g)
        cur_g.append(cur)
    return groups


def sortGroup(group: list[tuple]):
    values = []
    indices = []
    while group:
        a, b = group.pop()
        values.append(a)
        indices.append(b)
    indices.sort()
    while values:
        el = values.pop(), indices.pop()
        group.append(el)


def sortByGroup(groups: list[list[tuple]]):
    for i, e in enumerate(groups):
        sortGroup(e)
    return


def joinByGroups(groups: list[list[tuple]], nums: list[int]):
    nexgroup = {}
    while groups:
        cur_g = groups.pop()
        nexgroup[cur_g[-1][1]] = cur_g
    cur = 0
    while nexgroup:
        cur_g = nexgroup.pop(cur)
        nums.append(cur_g.pop()[0])
        cur += 1
        if not cur_g:
            continue
        nexgroup[cur_g[-1][1]] = cur_g
    return


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_enum = getSortedEnum(nums)
        groups = separateByLimit(sorted_enum, limit)
        if len(groups) == 1:
            while groups[0]:
                nums.append(groups[0].pop()[0])
            return nums
        sortByGroup(groups)
        joinByGroups(groups, nums)
        return nums

    main = lexicographicallySmallestArray


TESTS = [
    (
        ([6, 9, 4, 2, 0], 3),
        [0, 2, 4, 6, 9]
    )
    ,
    (
        ([6, 9, 4, 2, 0], 2),
        [0, 9, 2, 4, 6]
    )
    ,
    (
        ([6, 9, 4, 2, 0], 1),
        [6, 9, 4, 2, 0]
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
