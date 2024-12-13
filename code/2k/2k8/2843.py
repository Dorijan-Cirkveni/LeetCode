import bisect
import math


def sum9(digitCount: int, target: int):
    upper = digitCount + target - 1
    prefix = 1
    res = 0
    for i in range(target // 10 + 1):
        single_part = math.comb(upper, digitCount)
        part_count = math.comb(digitCount, i)
        res += single_part * part_count * prefix
        upper -= 10
        prefix *= -1
    return res


def sum9_brute(digit_count: int, target: int) -> int:
    if digit_count < 1:
        return int(target == 0)
    if digit_count == 1:
        return int(target in range(10))
    if digit_count == 2:
        return max(min(target, 19 - target), 0)
    return sum([sum9_brute(digit_count - 1, target - i) for i in range(10)])


def sum9_brute_stack(digit_count: int, target: int) -> int:
    if digit_count == 0:
        return int(target == 0)
    if digit_count == 1:
        return int(target in range(10))
    targets = [1]
    while digit_count > 2:
        nex_targets = [0] * (len(targets) + 9)
        for i, e in enumerate(targets):
            for j in range(i):
                nex_targets[j] += e
        targets = nex_targets
        target -= 9
    return sum([sum9_brute(digit_count - 1, target - i) for e in target])


#------------------------------------------------

ALL_FOR_DIGIT_COUNT = [[1]]


def step(L):
    L2 = [0] * (len(L) + 9)
    for i, e in enumerate(L):
        for i2 in range(i, i + 10):
            L2[i2] += e
    return L2


def get_x(count, ind):
    L = ALL_FOR_DIGIT_COUNT[count]
    if ind not in range(len(L)):
        return 0
    return L[ind]


for _ in range(4):
    ALL_FOR_DIGIT_COUNT.append(step(ALL_FOR_DIGIT_COUNT[-1]))


def sumDigits(n):
    s = 0
    while n:
        n, k = divmod(n, 10)
        s += k
    return s


def getLittleEndianQueue(n: int) -> list[int]:
    L = []
    while n:
        n, k = divmod(n, 10)
        L.append(k)
    return L


def countAllWithSum(base: int, limit, skip_zero=False):
    n_sum = sumDigits(base)
    digits = getLittleEndianQueue(limit)
    res = 0
    count = len(digits)
    while count:
        cur = digits.pop()
        count -= 1
        for i in range(n_sum - skip_zero, n_sum - cur, -1):
            temp=get_x(count,i)
            res += temp
        n_sum -= cur
        skip_zero = False
    res += n_sum == 0
    return res

def countAllInDigitCount(half_count, prefix=0):
    res = 0
    for ns in range(prefix, prefix+1+9 * half_count):
        c1 = get_x(half_count, ns)
        c2 = get_x(half_count - 1, ns)
        res += c1 * (c1 - c2)
    return res


def countSymmetric(n):
    if n<1001:
        return n//11
    s = str(n)
    n_len = len(s)
    res = 0
    half_len=(n_len>>1)|(n_len&1)
    for i in range(half_len):
        temp=countAllInDigitCount(i)
        res+=temp
    if n_len & 1 != 0:
        return res
    first_part = int(s[:half_len])
    second_part = int(s[half_len:])
    ten_power=int('9'*(half_len-1))+1
    for curfirst in range(ten_power,first_part):
        res += get_x(half_len,sumDigits(curfirst))
    res += countAllWithSum(first_part, second_part)
    return res


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = countSymmetric(high)
        res -= countSymmetric(low - 1)
        return res

    main = countSymmetricIntegers


TESTS = [
    (
        (100,10000),
        615
    )
    ,
    (
        (1, 100),
        9
    )
    ,

    (
        (1200, 1230),
        4
    )
    ,
    (
        (100,1782),
        44
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
        s=str(args)
        res = SOL.main(*args)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1} ({s})")
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))
    print(f"{count} out of {len(tests)} tests passed")

def test1():
    res = 0
    X = [
        (12, 30)
    ]
    for E in X:
        temp = countAllWithSum(*E)
        print(E, ":", temp)
        res += temp
    print(res)
    return


def main():
    """
    :return:
    """
    for i in range(5):
        print(countAllInDigitCount(i))
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
