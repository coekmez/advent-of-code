from functools import reduce
from operator import mul


def part_1(data):
    homework = []
    total = 0
    for line in data:
        homework.append(line.split())
    # transpose data because cephalopods are funny
    homework = list(map(list, zip(*homework)))
    for problem in homework:
        if problem[-1] == "*":
            ans = reduce(mul, map(int, problem[:-1]))
        else:
            ans = sum(map(int, problem[:-1]))
        total += ans

    return total


def part_2(data):
    pass


def solve(data):
    return part_1(data), part_2(data)
