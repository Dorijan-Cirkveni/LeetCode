from typing import *


class Solution:
    def __init__(self):
        self.requirements:dict[str,set] = {}
        self.usages:dict[str,set] = {}
    def add(self,recipe,ingredients):
        ingredients=set(ingredients)
        for ing in ingredients:
            self.usages.setdefault(ing,set()).add(recipe)
        self.requirements[recipe]=ingredients
    def use(self, element:str, returns:list):
        curset=self.usages.get(element,set())
        for usage in curset:
            reqs=self.requirements[usage]
            reqs.remove(element)
            if not reqs:
                returns.append(usage)
        return
    def findAllRecipes(self,
                       recipes: List[str],
                       ingredients: List[List[str]],
                       supplies: List[str]
    ) -> List[str]:
        self.requirements={}
        self.usages={}
        for el in zip(recipes,ingredients):
            self.add(*el)
        recipes=ingredients=None
        produced=[]
        while supplies:
            cur=supplies.pop()
            self.use(cur,produced)
        res=[]
        while produced:
            cur=produced.pop()
            self.use(cur,produced)
            res.append(cur)
        return res
    main = findAllRecipes


TESTS = [
    (
        ([0, 1], 1),
        "test"
    )
    ,
    (
        ([0, 1], 2),
        "also test"
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
