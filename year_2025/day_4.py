def part_1(data):
    data = [list(row) for row in data]
    count = 0
    out = [[row[i] for i in range(len(row))] for row in data]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == ".":
                continue
            # get submatrix of neighbours
            roll_neighbours_matrix = [
                row[max(0, j - 1) : min(len(row) + 1, j + 2)]
                for row in data[max(0, i - 1) : min(len(data) + 1, i + 2)]
            ]
            if roll_is_pickable(roll_neighbours_matrix):
                count += 1
                out[i][j] = "."
    return count, out


def part_2(data):
    count = 0
    while True:
        new_count, out = part_1(data)
        count += new_count
        data = out
        if new_count == 0:
            break

    return count


def roll_is_pickable(roll_neighbours_matrix):
    nb_neighbours = -1
    for row in roll_neighbours_matrix:
        nb_neighbours += row.count("@")
    return nb_neighbours < 4


def solve(data):
    return part_1(data)[0], part_2(data)
