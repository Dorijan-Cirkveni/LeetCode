from collections import defaultdict
from typing import *
import inspect


data={}
def getWithLimit(num:int,target:int):
    if (num,target) in data:
        return data
    num, rem=divmod(num,10)
    return res

def getAll(n,target):
    L=[]
    while n:
        n,r=divmod(n,10)
        L.append(r)
    while L:
        c=L.pop()
        res=getWithLimit()



class Solution:
    def countLow(self,low):
        s=str(low)
        k=len(s)>>1
        s1=s[:k]
        s2=s[k:][::-1]
        res=int(s1)
        res-=int(s2<s1)
        return res

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        high-=high==10000
        res=0
        len_a=len(str(low))
        len_b=len(str(high))
        len_a_ev=(len_a+1)&-2
        len_b_ev=len_b|1
        for i in range(len_a_ev+1,len_b_ev+1,2):
            res+=int('9'*(i>>1))
        if len_a==len_a_ev:
            res+=self.countLow(low)
        if len_b!=len_b_ev:
            res-=int('9'*(len_b_ev>>1))
            res+=self.countLow(high+1)
        return res

    main = countSymmetricIntegers


TESTS = [
    (
        (1,100),
        9
    )
    ,

    (
        (1, 100),
        9
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
