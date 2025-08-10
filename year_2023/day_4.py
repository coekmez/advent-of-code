def part_1(data):
    total = 0
    for line in data:
        found_start_pos = False
        my_numbers = []
        curr_num = []
        for c in line:
            if c != ':' and not found_start_pos:
                continue
            elif c == ':':
                found_start_pos = True
                continue
            else:
                if c.isdigit():
                    curr_num.append()
                if c == ' ' and len(curr_num) > 0:
                    pass



        occurrences = 0
        for num in my_numbers:
            if num in winning_numbers:
                occurrences += 1

        if occurrences >= 1:
            total += 2**(occurrences-1)
        else:
            total += 0

    return total

def solve(data):
    print(f"Part_1: {part_1(data)}")
    # print(f"Part_2: {part_2(data)}")