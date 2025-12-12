def part_1(data):
    occurences = 0
    dial_pos = 50
    for line in data:
        if line[0] == "R":
            dial_pos = (dial_pos + int(line[1:])) % 100
        else:
            dial_pos = (dial_pos - int(line[1:])) % 100
        if dial_pos == 0:
            occurences += 1

    return occurences


def part_2(data):
    occurences = 0
    dial_pos = 50
    for line in data:
        init_pos = dial_pos
        # get full rotations out of the way
        rotation = int(line[1:])
        occurences += rotation // 100

        # now we work with the partial rotation
        rotation = rotation % 100
        dial_pos = dial_pos + rotation if line[0] == "R" else dial_pos - rotation

        # check for crossing or ending at zero IF the initial dial position was not 0. otherwise we risk counting it twice.
        if init_pos != 0 and (dial_pos <= 0 or dial_pos > 99):
            occurences += 1

        # update proper dial position
        dial_pos = dial_pos % 100

    return occurences


def solve(data):
    return part_1(data), part_2(data)
