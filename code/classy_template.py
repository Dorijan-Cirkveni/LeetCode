from typing import *

class Example:
    def __init__(self,test:int):
        self.test=test
    def testfn(self,v):
        return v**2+self.test

null=None
MAINCLASS=Example

def testfn(functions:list[str],args:list[list]):
    functions.reverse()
    args.reverse()
    functions.pop()
    c_args=args.pop()
    cls:MAINCLASS=MAINCLASS(*c_args)
    res=[]
    while functions:
        c_fn=functions.pop()
        fn=MAINCLASS.__getattribute__(cls,c_fn)
        c_args=args.pop()
        cures=fn(*c_args)
        res.append(cures)
    return res

TESTS = [
    (
        ["","testfn"],
        [[1],[2]],
        [5]
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
