with open('day_2/input.txt', 'r') as f:
    val = f.read().splitlines()

limits = {'red': 12, 'green': 13, 'blue': 14}
games = dict()
total = 0

for line in val:
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

print(total)