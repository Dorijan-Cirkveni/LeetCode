from typing import *


class Solution:
    def __init__(self):
        self.ends = {}
        self.starts = {}
        self.queries = []

    def getLimits(self,queries):
        starts = {}
        ends = {}
        query_results=[]
        existing={}
        for a,b,v in queries:

            starts.setdefault(a, dict())[b]=i
            ends.setdefault(b, dict())[a]=i
            i+=1

        self.starts=starts
        self.ends=ends

    def getBest(self, nums:List[int]):
        cur_best=0
        cur_list=[]
        for i,e in enumerate(nums):
            starts=self.starts.get(i,set())
            if starts:
                cur_list+=list(starts)
                cur_list.sort()
            if e:
                for ind in cur_list:
                    e-=self.queries[ind]
                    if e>0:
                        continue
                    if cur_best<=ind:
                        cur_best=ind+1
                    break
                else:
                    return -1
            ends=self.ends.get(i,set())
            if ends:
                cur_list=[e for e in cur_list if e not in ends]
        return cur_best


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        self.queries = queries
        self.getLimits()
        res=self.getBest(nums)
        return res

    main = minZeroArray


TESTS = [
    (
        ([2,0,0,8,6],[[0,1,2],[0,3,1],[4,4,2],[0,1,2],[3,3,4],[2,3,1],[0,4,2],[3,4,3],[4,4,5],[0,4,3],[0,3,2],[0,3,1],[2,3,4],[3,4,3],[3,4,5]]),8
    )
    ,
    (
        ([7,6,8],[[0,0,2],[0,1,5],[2,2,5],[0,2,4]]),4
    )
    ,
    (
        ([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]),
        2
    ),
    (
        ([500000]*500000,[[0,500000-1,5]]*100000),
        100000
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
