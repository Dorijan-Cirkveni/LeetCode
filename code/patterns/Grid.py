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


def main():
    print("This is a template.")


if __name__ == "__main__":
    main()
