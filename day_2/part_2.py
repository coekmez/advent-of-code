with open('day_2/input.txt', 'r') as f:
    val = f.read().splitlines()


games = dict()
total = 0

for line in val:
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

print(total)
            