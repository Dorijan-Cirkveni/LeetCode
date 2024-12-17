from typing import *
import inspect


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter={e:0 for e in s}
        for e in s:
            counter[e]+=1
        keys=list(counter)
        keys.sort()
        last='@'
        res=''
        while keys:
            cur=keys.pop()
            cur_limit=repeatLimit
            if last!='@':
                if last>cur:
                    cur_limit=1
                keys.append(last)
                last='@'
            v=counter.pop(cur)
            v2=min(v,cur_limit)
            res+=cur*v2
            v-=v2
            if v!=0:
                last=cur
                counter[last]=v
        return res

    main = repeatLimitedString


TESTS = [
    (
        ("cczazcc",3),
        "zzcccac"
    )
    ,
    (
        ("aababab",2),
        "bbabaa"
    )
    ,
    (
        ("robnsdvpuxbapuqgopqvxdrchivlifeepy",2),
        "yxxvvuvusrrqqppopponliihgfeeddcbba"
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
