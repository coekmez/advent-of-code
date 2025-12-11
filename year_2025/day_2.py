from math import ceil


def part_1(data):
    # this one is just a single long line, so needs some processing
    data = data[0].split(",")
    invalid_sum = 0
    for line in data:
        # get range
        lower, higher = map(int, line.split("-"))
        # how many positions
        lower_nb_positions = len(str(lower))
        # we need an even number of positions to even consider the numbers
        if len(str(lower)) % 2 != 0:
            print(lower)
            lower = ceil(lower / (10**lower_nb_positions)) * (10**lower_nb_positions)
            print(lower)
            lower_nb_positions = len(str(lower))

        # duplicate the first half of numbers
        first_half_candidate = lower // 10 ** (lower_nb_positions // 2)
        candidate = (
            first_half_candidate * 10 ** (lower_nb_positions // 2)
            + first_half_candidate
        )
        while candidate <= higher:
            # print(candidate)
            invalid_sum += candidate
            # update candidate
            first_half_candidate = candidate // 10 ** (lower_nb_positions // 2) + 1
            candidate = (
                first_half_candidate * 10 ** (lower_nb_positions // 2)
                + first_half_candidate
            )

    return invalid_sum


def part_2(data):
    pass


def solve(data):
    print(f"Part_1: {part_1(data)}")
    print(f"Part_2: {part_2(data)}")
