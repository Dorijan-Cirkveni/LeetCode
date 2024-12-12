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

def sumDigits(n,ret:list):
    s=0
    while n:
        n,k=divmod(n,10)
        s+=k
        ret.append(k)
    return s

def countAllWithSum(n):
    digits=[]
    n_sum=sumDigits(n,digits)
    res=1
    while digits:
        cur=digits.pop()
        for i in range(n_sum,n_sum-cur):
            res+=get_x(len(digits),i)
        n_sum-=cur
    return res

def countSymmetric(n):
    digits=[]
    n_sum=sumDigits(n,digits)
    res=0
    for i in range(len(digits)>>2):
        tempres=0
        for cur in range(10**i,10**(i+1)):
            tempres+=countAllWithSum()





class Solution:
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
    res=0
    for i in range(10,100):
        temp=countAllWithSum(i)
        print(i,temp,end=';')
        res+=temp
    return


if __name__ == "__main__":
    main()
