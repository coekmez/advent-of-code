def part_1(data):
    total = 0

    width = len(data[0])
    length = len(data)
    slot_is_in_the_total = [[False] * width for i in range(length)]
    for i in range(length):
        for j in range(width):
            # look for symbols first
            if is_symbol(
                data[i][j]
            ):  # we found a symbol, look for adjacent digits for part numbers
                # check left
                total += check_line(i, j - 1, data, slot_is_in_the_total)
                # check right
                total += check_line(i, j + 1, data, slot_is_in_the_total)
                # check up-left
                total += check_line(i - 1, j - 1, data, slot_is_in_the_total)
                # check up
                total += check_line(i - 1, j, data, slot_is_in_the_total)
                # check up-right
                total += check_line(i - 1, j + 1, data, slot_is_in_the_total)
                # check down-left
                total += check_line(i + 1, j - 1, data, slot_is_in_the_total)
                # check down
                total += check_line(i + 1, j, data, slot_is_in_the_total)
                # check down-right
                total += check_line(i + 1, j + 1, data, slot_is_in_the_total)

    return total


def part_2(data):
    width = len(data[0])
    length = len(data)
    slot_is_in_the_total = [[False] * width for i in range(length)]
    total = 0
    for i in range(length):
        for j in range(width):
            # look for symbols first
            if is_symbol(
                data[i][j]
            ):  # we found a symbol, look for adjacent digits for part numbers
                parts = [
                    check_line(i, j - 1, data, slot_is_in_the_total),
                    check_line(i, j + 1, data, slot_is_in_the_total),
                    check_line(i - 1, j - 1, data, slot_is_in_the_total),
                    check_line(i - 1, j, data, slot_is_in_the_total),
                    check_line(i - 1, j + 1, data, slot_is_in_the_total),
                    check_line(i + 1, j - 1, data, slot_is_in_the_total),
                    check_line(i + 1, j, data, slot_is_in_the_total),
                    check_line(i + 1, j + 1, data, slot_is_in_the_total),
                ]

                parts = [part for part in parts if part > 0]

                if len(parts) == 2:
                    total += parts[0] * parts[1]

    return total


def is_symbol(c):
    if c.isdigit() or c == ".":
        return False
    return True


def is_in_bounds(row, column, max_row, max_column):
    if 0 <= row < max_row and 0 <= column < max_column:
        return True
    else:
        return False


def check_line(row, column, data, slot_is_in_the_total):
    if (
        data[row][column].isdigit()
        and is_in_bounds(row, column, len(data), len(data[0]))
        and not slot_is_in_the_total[row][column]
    ):
        part_number = [data[row][column]]
        slot_is_in_the_total[row][column] = True
        # check left
        cursor = column - 1
        while cursor >= 0 and data[row][cursor].isdigit():
            part_number.insert(0, data[row][cursor])
            slot_is_in_the_total[row][cursor] = True
            cursor -= 1  # move cursor to left

        # check right
        cursor = column + 1
        while cursor < len(data[0]) and data[row][cursor].isdigit():
            part_number.append(data[row][cursor])
            slot_is_in_the_total[row][cursor] = True
            cursor += 1  # move cursor to right

        return int("".join(part_number))
    else:
        return 0


def solve(data):
    return part_1(data), part_2(data)
