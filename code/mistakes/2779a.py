from collections import deque
from typing import *
import inspect

def handleMonotonic(stack:list[tuple[int,int]],ind,v,prefix:int):
    while stack:
        cur_ind,cur=stack.pop()
        match (v-cur)*prefix:
            case 0:
                ind=cur_ind
                break
            case c if c<0:
                stack.append((cur_ind,cur))
                break
    stack.append((ind,v))
    return len(stack)-1



class Solution:
    def findFurthest(self,lower_ind,upper_ind):
        lower_bound=self.lower_bound
        upper_bound=self.upper_bound
        A=lower_bound[lower_ind]
        B=upper_bound[upper_ind]
        while A[1]>B[1]:
            if A[0]<B[0]:
                lower_ind+=1
                A=lower_bound[lower_ind]
            else:
                upper_ind+=1
                B=upper_bound[upper_ind]
        return lower_ind,upper_ind,min(A[0],B[0])

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        cur_ind=1
        cur=nums.pop()
        lower_ind=0
        self.lower_bound=[(0,cur-k)]
        upper_ind=0
        self.upper_bound=[(0,cur+k)]
        first=0
        best=0
        while nums:
            cur=nums.pop()
            temp=handleMonotonic(self.lower_bound,cur_ind,cur-k,1)
            lower_ind=min(lower_ind,temp)
            temp=handleMonotonic(self.upper_bound,cur_ind,cur+k,-1)
            upper_ind=min(upper_ind,temp)
            lower_ind,upper_ind,cur_first=self.findFurthest(lower_ind,upper_ind)
            if first==cur_first:
                best=cur_ind-first+1
            else:
                first=cur_first
            cur_ind+=1
        return best
    main = maximumBeauty


TESTS = [
    (
        ([4,6,1,2], 2),
        3
    )
    ,
    (
        ([0, -1, 2, 3, 9], 2),
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
