from collections import deque
from typing import *


class LRUCache:

    def __init__(self, capacity: int):
        self.values: dict = dict()

        self.capacity: int = capacity
        self.evicted: int = 0
        self.lru: deque = deque()
        self.count: dict = dict()

    def passive_clear_evictions(self):
        if self.evicted > self.capacity:
            self.active_clear_evictions()
        while self.lru:
            cur = self.lru.popleft()
            if self.count[cur] == 1:
                self.lru.appendleft(cur)
                break
            self.count[cur] -= 1
            self.evicted -= 1

    def active_clear_evictions(self):
        self.evicted = 0
        new_lru = deque()
        while self.lru:
            cur = self.lru.popleft()
            if self.count[cur] == 1:
                new_lru.append(cur)
            else:
                self.count[cur] -= 1
        self.lru = new_lru
        self.evicted = 0

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self.count[key] += 1
        self.lru.append(key)
        self.evicted += 1
        self.passive_clear_evictions()
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        self.lru.append(key)
        if key not in self.values:
            self.count[key] = 1
            if self.capacity:
                self.capacity -= 1
            else:
                last = self.lru.popleft()
                self.values.pop(last)
        else:
            self.count[key] += 1
            self.evicted += 1
        self.values[key] = value
        self.passive_clear_evictions()
        return


null = None
MAINCLASS = LRUCache


def testfn(functions: list[str], args: list[list]):
    functions.reverse()
    args.reverse()
    functions.pop()
    c_args = args.pop()
    cls: MAINCLASS = MAINCLASS(*c_args)
    res = [null]
    while functions:
        c_fn = functions.pop()
        fn = MAINCLASS.__getattribute__(cls, c_fn)
        c_args = args.pop()
        cures = fn(*c_args)
        res.append(cures)
    return res


TESTS = [
    (
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]],
        [null,-1,null,-1,null,null,2,6]
    )
    ,
    (
        ["LRUCache", "put", "get", "put", "get", "get"],
        [[1], [2, 1], [2], [3, 2], [2], [3]],
        [null,null,1,null,-1,2]
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
