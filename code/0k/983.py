import heapq
from typing import *
import inspect


class InverseMinimumPriorityQueue:
    def __init__(self, values:dict):
        self.queue=[-e for e in values]
        heapq.heapify(self.queue)
        self.values=values
    def push(self,key,value):
        if key not in self.values:
            heapq.heappush(self.queue,-key)
        elif self.values[key]<=value:
            return
        self.values[key]=value
    def pop(self):
        key=-heapq.heappop(self.queue)
        value=self.values.pop(key)
        return key,value
    def isReady(self,ref):
        return -self.queue[0]>=ref


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        nex_days=InverseMinimumPriorityQueue({420:0,-1:1<<31})
        costs=list(zip(costs,[1,7,30]))
        while days:
            today=days.pop()
            early=set()
            while nex_days.isReady(today):
                early.add(nex_days.pop()[1])
            if not early:
                continue
            early=min(early)
            for cost,time in costs:
                nex_time=today-time
                nex_cost=early+cost
                nex_days.push(nex_time,nex_cost)
        return min(nex_days.values.values())

    main = mincostTickets


TESTS = [
    (
        ([1,4,6,7,8,20], [2,7,15]),
        11
    )
    ,
    (
        ([1,4,6,7,8,20], [2,7,15]),
        11
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
