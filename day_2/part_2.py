with open('puzzle_2/input.txt', 'r') as f:
    input = f.read().splitlines()


games = dict()
sum = 0

for line in input:
    limits = {'red': 0, 'green': 0, 'blue': 0}
    id = int(line.split(':')[0].split(' ')[-1])
    subsets = line.split(':')[-1].split(';')
    for subset in subsets:
        subset_dict = dict()
        data = subset.split(',')
        for entry in data:
            _, number, color = entry.split(' ')
            if limits[color] < int(number):
                limits[color] = int(number)
    sum += limits['red'] * limits['blue'] * limits['green']

print(sum)
            