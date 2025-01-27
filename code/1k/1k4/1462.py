from typing import *


class Course:
    def __init__(self):
        self.allows = set()
        self.level = -1


class Solution:
    def __init__(self):
        self.courses: dict[int, Course] = {}
        self.n = -1
        self.finals = set()

    def buildAllows(self, prerequisites):
        used = set()
        while prerequisites:
            a, b = prerequisites.pop()
            used.add(b)
            self.courses.setdefault(a, Course()).allows.add(b)
        return used

    def buildLevels(self, used):
        curset = set(self.courses) - used
        level = 0
        while curset:
            nexset = set()
            for ind in curset:
                course = self.courses.setdefault(ind, Course())
                course.level = level
                nexset |= course.allows
            curset = nexset
            level += 1

    def checkIfAllows(self, a, b):
        if a == b:
            return True
        course_a: Course = self.courses.get(a)
        if course_a is None:
            return False
        course_b: Course = self.courses.get(b)
        if course_b is None:
            return False
        diff = course_b.level - course_a.level
        if diff <= 0:
            return False
        curset = {a}
        for i in range(diff - 1):
            nexset = set()
            for el in curset:
                allows = self.courses[el].allows
                if b in allows:
                    return True
                nexset |= allows
            curset = nexset
        for el in curset:
            if b in self.courses[el].allows:
                return True
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        self.n = numCourses
        self.courses = {}
        used = self.buildAllows(prerequisites)
        self.buildLevels(used)
        queries.reverse()
        res = []
        while queries:
            cures = self.checkIfAllows(*queries.pop())
            res.append(cures)
        return res

    main = checkIfPrerequisite


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
