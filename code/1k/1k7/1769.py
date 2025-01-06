from typing import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        count = cures = 0
        for e in boxes:
            count += e == '1'
            cures += count
        res = []
        for e in boxes[::-1]:
            cures -= count
            if e == '1':
                count -= 2
            res.append(cures)
        res.reverse()
        return res

    main = minOperations


TESTS = [
    (
        ("110",),
        [1,1,3]
    )
    ,
    (
        ("001011",),
        [11,8,5,4,3,4]
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
