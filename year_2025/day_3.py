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
    sum = 0
    for line in data:
        num = []
        left_index = 0
        right_index = len(line) - 11
        while len(num) < 12:
            max_num = max(line[left_index:right_index])
            num.append(max_num)
            left_index += line[left_index:right_index].index(max_num) + 1
            right_index += 1

        jolts = int("".join(num))
        sum += jolts

    return sum


def solve(data):
    return part_1(data), part_2(data)
