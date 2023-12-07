with open('puzzle_1/input.txt', 'r') as f:
    input = f.read().splitlines()

nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
total = 0
for s in input:
    number = []
    for c in s:
        if c in nums:
            number.append(c)
    if len(number) > 0:
        number = 10 * int(number[0]) + int(number[-1])
        total += number

print(total)