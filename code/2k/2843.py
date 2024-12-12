import bisect
import math


def sum9(digitCount:int,target:int):
    upper=digitCount+target-1
    prefix=1
    res=0
    for i in range(target//10+1):
        single_part=math.comb(upper,digitCount)
        part_count=math.comb(digitCount,i)
        res+=single_part*part_count*prefix
        upper-=10
        prefix*=-1
    return res

def sum9_brute(digit_count:int, target:int)->int:
    if digit_count<1:
        return int(target==0)
    if digit_count==1:
        return int(target in range(10))
    if digit_count==2:
        return max(min(target,19-target),0)
    return sum([sum9_brute(digit_count-1,target-i) for i in range(10)])

def sum9_brute_stack(digit_count:int, target:int)->int:
    if digit_count==0:
        return int(target==0)
    if digit_count==1:
        return int(target in range(10))
    targets=[1]
    while digit_count>2:
        nex_targets=[0]*(len(targets)+9)
        for i,e in enumerate(targets):
            for j in range(i):
                nex_targets[j]+=e
        targets=nex_targets
        target-=9
    return sum([sum9_brute(digit_count-1,target-i) for e in target])

#------------------------------------------------

X=[[1]]
def step(L):
    L2=[0]*(len(L)+9)
    for i,e in enumerate(L):
        for i2 in range(i,i+9):
            L2[i2]+=e
    return L2
def get_x(count,ind):
    L=X[count]
    if ind not in range(len(L)):
        return 0
    return L[ind]
for _ in range(4):
    X.append(step(X[-1]))

def sumDigits(n):
    s=0
    while n:
        n,k=divmod(n,10)
        s+=k
    return s

def getLittleEndianQueue(n:int)->list[int]:
    L=[]
    while n:
        n,k=divmod(n,10)
        L.append(k)
    return L

def countAllWithSum(base:int,limit,skip_zero=False):
    n_sum=sumDigits(base)
    digits=getLittleEndianQueue(limit)
    res=0
    count=len(digits)
    while count:
        cur=digits.pop()
        count-=1
        for i in range(n_sum-skip_zero,n_sum-cur,-1):
            temp=get_x(count,i)
            res+=temp
        n_sum-=cur
        skip_zero=False
    res+=n_sum==0
    return res

def countSymmetric(n):
    s=str(n)
    n_len=len(s)
    res=0
    for i in range(2,n_len+2,2):
        tempres=0
        for ns in range(1,9*i):
            c1=get_x(i,ns,True)
            tempres+=c1*(c1-c2)
        res+=tempres
    if n_len&1==0:
        first_part=int(s[:n_len>>2])
        second_part=int(s[n_len>>2:])
        res+=countAllWithSum(first_part,second_part)
    return res





class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=countSymmetric(high)
        res-=countSymmetric(low-1)
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
    res=0
    X=[
        (12,30)
    ]
    for E in X:
        temp=countAllWithSum(*E)
        print(E,":",temp)
        res+=temp
    print(res)
    return


if __name__ == "__main__":
    main()
