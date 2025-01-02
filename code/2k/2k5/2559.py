from typing import *
import inspect


vowelset=set('aeiou')
def isvowel(word):
    if word[0] not in vowelset:
        return 0
    if word[-1] not in vowelset:
        return 0
    return 1
def reverse_acc_vowel(words):
    words.reverse()
    acc=0
    vowel_acc=[]
    while words:
        cur=words.pop()
        acc+=isvowel(cur)
        vowel_acc.append(acc)
    vowel_acc.append(0)
    return vowel_acc
def process_queries(vowel_acc,queries):
    queries.reverse()
    res=[]
    while queries:
        a,b=queries.pop()
        cur=vowel_acc[b]-vowel_acc[a-1]
        res.append(cur)
    return res
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_acc=reverse_acc_vowel(words)
        res=process_queries(vowel_acc,queries)
        return res

    main = vowelStrings


TESTS = [
    (
        (["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]),
        [2,3,0]
    )
    ,
    (
        (["a","e","i"], [[0,2],[0,1],[2,2]]),
        [3,2,1]
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
