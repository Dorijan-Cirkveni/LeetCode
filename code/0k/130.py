from typing import *
import inspect


class Solution:
    def __init__(self):
        self.M:list[list[str]]=[]
    def get(self,i,j):
        return self.M[i][j]
    def get_neigh(self,i:int,j:int,cur:str,nexset:set,border_set:set):
        for cd in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]:
            val=self.get(*cd)
            if val.upper() == cur:
                nexset.add(cd)
            else:
                border_set.add(val)

    def traverse(self,start:tuple,val:str,change_to:str)->set:
        curset={start}
        border_set=set()
        while curset:
            nexset=set()
            for i,j in curset:
                self.M[i][j]=change_to
                self.get_neigh(i,j,val,nexset,border_set)
            curset=nexset
        return border_set


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.M=board
        e=[]
        for e in board:
            e.append('')
        self.M.append(['']*len(e))
        for i,E in enumerate(board):
            for j,e in enumerate(E):
                if e!='O':
                    continue
                curset=self.traverse((i,j),e,'A')
                nex='o' if '' in curset else 'X'
                self.traverse((i,j),'A',nex)
        for E in board:
            E.pop()
            for i,e in enumerate(E):
                if e=='o':
                    E[i]='O'
        board.pop()
        return

    main = solve


TESTS = [
    (
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    )
]

def to_str(M):
    L=[]
    for E in M:
        L.append(''.join(E))
    return '\n'.join(L)

def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
    for i, (res, true_res) in enumerate(tests):
        SOL.main(res)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1}")
        print(f"Got\n{to_str(res)}")
        print(f"Expected \n{to_str(true_res)}")
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
