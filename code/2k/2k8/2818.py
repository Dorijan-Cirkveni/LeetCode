from typing import *

PRIMES = [3, 5, 7]
MOD = 10 ** 9 + 7


def generatePrimes(target: int):
    i = PRIMES[-1]
    while True:
        i += 2
        for e in PRIMES:
            if i % e == 0:
                break
        else:
            PRIMES.append(i)
            if i >= target:
                return


generatePrimes(10000)


def getPrimeScore(num: int) -> int:
    score = 1 ^ (num % 2)
    while num & 1 == 0:
        num >>= 1
    for e in PRIMES:
        if e * e > num:
            break
        if num % e != 0:
            continue
        score += 1
        num //= e
        while num % e == 0:
            num //= e
    score += num != 1
    return score


class Solution:
    def __init__(self):
        self.prime_scores: dict[int, int] = {}
        self.nums: list[int] = []

    def getPrimeScores(self):
        self.prime_scores = {}
        for e in self.nums:
            if e not in self.prime_scores:
                self.prime_scores[e] = getPrimeScore(e)

    def createLeft(self, nums):
        stack = [(9999, -1)]
        left = []
        for i, e in enumerate(nums):
            v = self.prime_scores[e]
            while stack[-1][0] < v:
                stack.pop()
            cur = stack[-1][1]
            left.append(cur)
            stack.append((v, i))
        return left

    def createRight(self, nums):
        stack = [(9999, len(nums))]
        right = []
        for i in range(len(nums) - 1, -1, -1):
            e = nums[i]
            v = self.prime_scores[e]
            while stack[-1][0] <= v:
                stack.pop()
            cur = stack[-1][1]
            right.append(cur)
            stack.append((v, i))
        right.reverse()
        return right

    def maximumScore(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.getPrimeScores()
        left = self.createLeft(nums)
        right = self.createRight(nums)
        enumerated = [(e, i) for i, e in enumerate(nums)]
        enumerated.sort()
        ans = 1
        while k and enumerated:
            e, i = enumerated.pop()
            lel, rel = left[i], right[i]
            cnt = (i - lel) * (rel - i)
            if cnt > k:
                cnt = k
            ans *= pow(e, cnt, MOD)
            ans %= MOD
            k -= cnt
        return ans

    main = maximumScore


TESTS = [
    (
        ([8, 3, 9, 3, 8], 2),
        81
    )
    ,
    (
        ([19, 12, 14, 6, 10, 18], 3),
        4788
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
