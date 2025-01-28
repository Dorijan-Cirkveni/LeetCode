from typing import *

class Grid:
    def __init__(self,core:list[list],deepcopy=False):
        if deepcopy:
            core=[[f for f in e] for e in core]
        self.n=len(core)
        self.m=len(core[0])
        self.core=core
    def sentinels(self,value:int,width:int=1):
        for e in self.core:
            e+=[value]*width
        self.core+=[[value]*(self.m+width)]*width
    def getTile(self,i,j):
        return self.core[i][j]
    def setTile(self,i,j,v):
        self.core[i][j]=v
    def popTile(self,i:int,j:int,v=0):
        line=self.core[i]
        v=line[j]
        line[j]=0
        return v
    def getNeigh(self,i:int,j:int):
        return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    def getValidNeigh(self,el:tuple,sentinels:set[int],output_method:callable):
        for nel in self.getNeigh(*el):
            val=self.getTile(*nel)
            if val in sentinels:
                continue
            output_method(nel)
    def clearIsland(self,start:tuple):
        curset={start}
        res=0
        while curset:
            nexset=set()
            for cur in curset:
                res+=self.popTile(*cur)
                self.getValidNeigh(cur,sentinels={0},output_method=nexset.add)
            curset=nexset
        return res
    def clearAllIslands(self):
        if len(self.core)==self.n:
            self.sentinels(0)
        res=0
        for i in range(self.n):
            for j in range(self.m):
                if self.getTile(i,j)==0:
                    continue
                cur=self.clearIsland((i,j))
                if res<cur:
                    res=cur
        return res

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        return Grid(grid).clearAllIslands()


    main = findMaxFish


TESTS = [
    (
        ([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]], ),
        7
    )
    ,
    (
        ([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],),
        1
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
