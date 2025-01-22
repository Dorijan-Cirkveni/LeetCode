from typing import *


INF=2001


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        cur_list:list[tuple]=[]
        for i,line in enumerate(isWater):
            for j,el in enumerate(line):
                if not el:
                    continue
                line[j]=0 if el else INF
                cur_list.append((i,j))
            line.append(INF)
        isWater.append([INF]*len(isWater[0]))
        height=0
        while cur_list:
            height+=1
            nex_list=[]
            while cur_list:
                i,j=cur_list.pop()
                nex_temp=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                for di,dj in nex_temp:
                    if isWater[di][dj]==height:
                        continue
                    isWater[di][dj]=height
                    nex_list.append((di,dj))
            cur_list=nex_list
        isWater.pop()
        for line in isWater:
            line.pop()
        return isWater

    main = highestPeak


TESTS = [
    (
        ([[0,1],[0,0]],),
        [[1,0],[2,1]]
    )
    ,
    (
        ([[0,0,1],[1,0,0],[0,0,0]],),
        [[1,1,0],[0,1,1],[1,2,2]]
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
