def part_1(data):
    sum = 0
    for line in data:
        big_digit = int(line[0])
        small_digit = 0
        for i in range(1, len(line)):
            candidate = int(line[i])
            if candidate > small_digit:
                small_digit = candidate
            if candidate > big_digit and i < (len(line) - 1):
                big_digit = candidate
                small_digit = 0
        num = big_digit * 10 + small_digit
        sum += num
    return sum


def part_2(data):
    num = []


def solve(data):
    return part_1(data), part_2(data)
