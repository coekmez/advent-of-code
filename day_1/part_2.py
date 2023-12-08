with open('day_1/input.txt', 'r') as f:
    input = f.read().splitlines()

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
stringy_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0
for line in input:
    # find first number
    cursor = 1
    first_digit_found = False
    while(not first_digit_found):
        temp = line[:cursor]
        if temp[-1] in nums:
            first_digit = nums.index(temp[-1])
            first_digit_found = True
        for stringy_num in stringy_nums:
            if stringy_num in temp:
                first_digit = stringy_nums.index(stringy_num)
                first_digit_found = True
        cursor += 1

    # find last number
    cursor = -1
    last_digit_found = False
    while(not last_digit_found):
        temp = line[cursor:]
        if temp[0] in nums:
            last_digit = nums.index(temp[0])
            last_digit_found = True
        for stringy_num in stringy_nums:
            if stringy_num in temp:
                last_digit = stringy_nums.index(stringy_num)
                last_digit_found = True
        cursor -= 1

    total += 10*first_digit + last_digit


print(total)