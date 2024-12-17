def makeTwos(nums:list[int]):
    lim=len(nums)
    twos=[set() for _ in range(lim)]
    acc=0
    lim-=1
    for i,e in enumerate(nums):
        cur=0
        for j in range(i,lim if i else i):
            cur*=10
            cur+=nums[j]
            twos[j+1].add((acc,cur))
            if cur==0:
                break
        if i and not acc:
            break
        acc*=10
        acc+=e
    return twos

def tailCheck(nums:list[int],a:int,b:int,size:int):
    c=0
    for i in range(size,len(nums)):
        c*=10
        c+=nums[i]
        if c==0:
            return False
        if c==a+b:
            a=b
            b=c
            c=0
    return c==0

def checkThrees(nums:list[int],twos:list[set]):
    for i,curset in enumerate(twos):
        for el in curset:
            if tailCheck(nums,*el,size=i):
                return True
    return False

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if num[:2]=='00':
            return len(set(num))==1
        nums=[int(e) for e in num]
        twos=makeTwos(nums)
        res=checkThrees(nums,twos)
        return res
    main = isAdditiveNumber


TESTS = [
    (
        ("000000",),
        True
    )
    ,
    (
        ("011235",),
        True
    )
    ,
    (
        ("000",),
        True
    )
    ,
    (
        ("199100199",),
        True
    )
    ,
    (
        ("101",),
        True
    )
    ,
    (
        ("123",),
        True
    )
    ,
    (
        ("112358",),
        True
    )
    ,
    (
        ("113",),
        False
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
