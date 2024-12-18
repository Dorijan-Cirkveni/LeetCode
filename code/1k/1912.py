import heapq
from collections import defaultdict
from typing import *
import inspect


class KeepTrackOfBest:
    def __init__(self):
        self.items:dict=dict()
        self.best=[]
        self.removed=set()

    def add(self,key,value):
        self.items[key]=value
        heapq.heappush(self.best,(value,key))

    def pop(self,key):
        value=self.items.pop(key)
        self.removed.add(key)
        if not self.items:
            self.__init__()
            return value
        while self.best[0][1] in self.removed:
            _,cur=heapq.heappop(self.best)
            self.removed.remove(cur)
        if (len(self.removed)<<1)>len(self.best):
            self.best=[E for E in self.best if E[1] not in self.removed]
            heapq.heapify(self.best)
            self.removed=set()
        return value

    def get_best(self,n=5):
        res=[]
        temp=[]
        while n and self.best:
            value,key=heapq.heappop(self.best)
            if key in self.removed:
                self.removed.remove(key)
                continue
            n-=1
            temp.append((value,key))
            res.append(key)
        while temp:
            el=temp.pop()
            heapq.heappush(self.best,el)
        return res




class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.by_movie_avail = {}
        while entries:
            shop, movie, price = entries.pop()
            movielist:KeepTrackOfBest =self.by_movie_avail.setdefault(movie,KeepTrackOfBest())
            movielist.add(shop,price)
        self.rented=KeepTrackOfBest()

    def search(self, movie: int, *_args) -> List[int]:
        if movie not in self.by_movie_avail:
            return []
        movielist:KeepTrackOfBest=self.by_movie_avail[movie]
        res=movielist.get_best(5)
        return res

    def rent(self, shop: int, movie: int, *_args) -> None:
        assert movie in self.by_movie_avail
        movielist:KeepTrackOfBest=self.by_movie_avail[movie]
        price=movielist.pop(shop)
        self.rented.add((movie,shop),price)


    def drop(self, shop: int, movie: int, *_args) -> None:
        price=self.rented.pop((movie,shop))
        movielist:KeepTrackOfBest=self.by_movie_avail.setdefault(movie,KeepTrackOfBest())
        movielist.add(shop,price)


    def report(self, *_args) -> List[List[int]]:
        best_rented=self.rented.get_best(5)
        return [[b,a] for (a,b) in best_rented]

    # Your MovieRentingSystem object will be instantiated and called as such:
    # obj = MovieRentingSystem(n, entries)
    # param_1 = obj.search(movie)
    # obj.rent(shop,movie)
    # obj.drop(shop,movie)
    # param_4 = obj.report()

fn_map={
    'rent':MovieRentingSystem.rent,
    'drop':MovieRentingSystem.drop,
    'search':MovieRentingSystem.search,
    'report':MovieRentingSystem.report
}

def testfn(functions:list[str],args:list[list]):
    functions.reverse()
    args.reverse()
    functions.pop()
    c_args=args.pop()
    cls:MovieRentingSystem=MovieRentingSystem(*c_args)
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
