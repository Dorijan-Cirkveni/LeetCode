from typing import *

class Example:
    def __init__(self,test:int):
        self.test=test


MAINCLASS=Example

fn_map=

def testfn(functions:list[str],args:list[list]):
    functions.reverse()
    args.reverse()
    functions.pop()
    c_args=args.pop()
    cls:MAINCLASS=MAINCLASS(*c_args)
    res=[]
    while functions:
        c_fn=functions.pop()
        fn=fn_map.get(c_fn,print)
        c_args=args.pop()
        cures=fn(cls,*c_args)
        res.append(cures)
    return res

TESTS = [
    (
        ["MovieRentingSystem","search","rent","rent","report","drop","search"],
        [[3,[[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]]],[1],[0,1],[1,2],[],[1,2],[2]],
        [[1, 0, 2], None, None, [[0, 1], [1, 2]], None, [0, 1]]
    )
    ,
    (
        ["MovieRentingSystem","rent","drop","rent","rent","rent","drop","search","report","rent","search"],
[[10,[[4,374,55],[1,6371,21],[8,3660,24],[1,56,32],[5,374,71],[3,4408,36],[6,9322,73],[6,9574,92],[8,7834,62],[2,6084,27],[7,3262,89],[2,8959,53],[0,3323,41],[6,6565,45],[0,4239,20]]],[0,4239],[0,4239],[3,4408],[2,6084],[0,4239],[0,4239],[9346],[],[6,9322],[8698]],
        []
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    count = 0
    print("Running...")
    for i, (functions, args, true_res) in enumerate(tests):
        res = testfn(functions, args)
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
