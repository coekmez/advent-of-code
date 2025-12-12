from math import ceil


def part_1(data):
    # this one is just a single long line, so needs some processing
    data = data[0].split(",")
    invalids = []
    for line in data:
        # get range
        lower, higher = map(int, line.split("-"))
        # how many positions
        lower_nb_positions = len(str(lower))
        # we need an even number of positions to even consider the numbers
        if len(str(lower)) % 2 != 0:
            lower = ceil(lower / (10**lower_nb_positions)) * (10**lower_nb_positions)
            lower_nb_positions = len(str(lower))

        # duplicate the first half of numbers
        first_half_candidate = str(lower)[: lower_nb_positions // 2]
        candidate = int(first_half_candidate + first_half_candidate)
        # find the first valid candidate
        while candidate < lower:
            first_half_candidate = str(
                int(str(candidate)[: lower_nb_positions // 2]) + 1
            )
            candidate = candidate = int(first_half_candidate + first_half_candidate)
        # we found the candidate past the lower limit now. we go until the upper end
        while candidate <= higher:
            # print(candidate)
            invalids.append(candidate)
            # update candidate
            first_half_candidate = str(
                int(str(candidate)[: lower_nb_positions // 2]) + 1
            )
            candidate = candidate = int(first_half_candidate + first_half_candidate)
    return sum(invalids)


def part_2(data):
    # this one is just a single long line, so needs some processing
    data = data[0].split(",")
    invalids = []
    for line in data:
        # get range
        init_lower, higher = map(int, line.split("-"))
        # how many positions
        lower_nb_positions = len(str(init_lower))
        for i in range(2, len(str(higher)) + 1):
            # check number of positions, it should be divisible by i as we check for i repetitions
            if len(str(init_lower)) % i != 0:
                if len(str(init_lower)) < i:
                    lower = 10 ** (i - 1)
                else:
                    lower = 10 ** (
                        len(str(init_lower)) + i - (len(str(init_lower)) % i) - 1
                    )
                lower_nb_positions = len(str(lower))
            else:
                lower = init_lower

            # eliminate illogical case where lower > higher
            if lower > higher:
                continue

            # duplicate the first half of numbers
            first_half_candidate = str(lower)[: lower_nb_positions // i]
            candidate = first_half_candidate
            for j in range(i - 1):
                candidate += first_half_candidate
            candidate = int(candidate)
            # find the first valid candidate
            while candidate < lower:
                first_half_candidate = str(
                    int(str(candidate)[: lower_nb_positions // i]) + 1
                )
                candidate = first_half_candidate
                for j in range(i - 1):
                    candidate += first_half_candidate
                candidate = int(candidate)
            # we found the candidate past the lower limit now. we go until the upper end
            while candidate <= higher:
                # print(candidate)
                if candidate not in invalids:
                    invalids.append(candidate)
                # update candidate
                first_half_candidate = str(
                    int(str(candidate)[: lower_nb_positions // i]) + 1
                )
                candidate = first_half_candidate
                for j in range(i - 1):
                    candidate += first_half_candidate
                candidate = int(candidate)
    return sum(set(invalids))


def solve(data):
    return part_1(data), part_2(data)
