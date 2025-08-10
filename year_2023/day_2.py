def part_1(data):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    games = dict()
    total = 0

    for line in data:
        faulty = False
        val_id = int(line.split(':')[0].split(' ')[-1])
        subsets = line.split(':')[-1].split(';')
        for subset in subsets:
            subset_dict = dict()
            data = subset.split(',')
            for entry in data:
                _, number, color = entry.split(' ')
                if limits[color] < int(number):
                    faulty = True
                    break
            if faulty:
                break
        if faulty:
            continue
        else:
            total += val_id

    return total

def part_2(data):
    games = dict()
    total = 0

    for line in data:
        limits = {'red': 0, 'green': 0, 'blue': 0}
        val_id = int(line.split(':')[0].split(' ')[-1])
        subsets = line.split(':')[-1].split(';')
        for subset in subsets:
            subset_dict = dict()
            data = subset.split(',')
            for entry in data:
                _, number, color = entry.split(' ')
                if limits[color] < int(number):
                    limits[color] = int(number)
        total += limits['red'] * limits['blue'] * limits['green']

    return total

def solve(data):
    print(f"Part_1: {part_1(data)}")
    print(f"Part_2: {part_2(data)}")