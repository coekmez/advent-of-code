def part_1(data):
    range_mode = True
    fresh_ids = []
    count = 0
    for line in data:
        if len(line) == 0:
            range_mode = False
            continue
        if range_mode:
            curr_min, curr_max = map(int, line.split("-"))
            fresh_ids.append((curr_min, curr_max))
        else:
            item_id = int(line)
            for curr_min, curr_max in fresh_ids:
                if curr_min <= item_id <= curr_max:
                    count += 1
                    break
    return count


def part_2(data):
    fresh_ids = []
    for line in data:
        if len(line) == 0:
            break
        curr_min, curr_max = map(int, line.split("-"))
        fresh_ids.append([curr_min, curr_max])

    # sort based on first element
    fresh_ids.sort(key=lambda x: x[0])
    merged_intervals = [fresh_ids[0]]
    for curr_min, curr_max in fresh_ids[1:]:
        # try to merge
        if merged_intervals[-1][0] <= curr_min <= merged_intervals[-1][-1]:
            if curr_max > merged_intervals[-1][-1]:
                merged_intervals[-1][-1] = curr_max
            else:
                continue
        else:
            merged_intervals.append([curr_min, curr_max])

    count = 0
    for curr_min, curr_max in merged_intervals:
        count += curr_max - curr_min + 1

    return count


def solve(data):
    return part_1(data), part_2(data)
