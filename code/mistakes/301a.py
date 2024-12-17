




def apply(el:tuple[int,int,int,bool], k:int, ret:set=None):
    if ret is None:
        ret = set()
    a,b,c,is3=el
    if c==0 and k==0:
        return
    if c==-1:
        c=0
    c2=c*10+k
    target=b<<1
    target-=a
    if (a==-1 or c2<=target//10) and c2:
        el=a,b,c2,is3
        ret.add(el)
    if a==-1 or c2==target:
        el=b,c,-1,is3 or a!=-1
        ret.add(el)

def step(curset:set,k:int):
    nexset=set()
    for el in curset:
        apply(el,k,nexset)
    return nexset

def solve(curset:set):
    for _,_,c,is3 in curset:
        if is3 and c==-1:
            return True
    return False

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        curset={(-1,-1,0,False)}
        for e in num:
            k=int(e)
            curset=step(curset,k)
            print(curset)
        res=solve(curset)
        return res

    main = isAdditiveNumber


TESTS = [
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
