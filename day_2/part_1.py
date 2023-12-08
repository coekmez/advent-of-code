with open('day_2/input.txt', 'r') as f:
    input = f.read().splitlines()

limits = {'red': 12, 'green': 13, 'blue': 14}
games = dict()
sum = 0

for line in input:
    faulty = False
    id = int(line.split(':')[0].split(' ')[-1])
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
        sum += id

print(sum)