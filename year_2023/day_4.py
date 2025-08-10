def part_1(data):
    total = 0
    for line in data:
        my_numbers = []
        curr_num = []
        winning_numbers = set()
        counting_winning_numbers = False
        counting_my_numbers = False
        for i in range(len(line)):
            c = line[i]
            if c != ':' and not counting_winning_numbers and not counting_my_numbers:
                continue
            elif c == ':':
                counting_winning_numbers = True
                continue
            elif c == '|':
                counting_winning_numbers = False
                counting_my_numbers = True
                continue
            else:
                if c.isdigit():
                    curr_num.append(c)
                if (c == ' ' or i==len(line)-1) and len(curr_num) > 0:
                    if counting_winning_numbers:
                        winning_numbers.add(int(''.join(curr_num)))
                    elif counting_my_numbers:
                        my_numbers.append(int(''.join(curr_num)))
                    else:
                        raise ValueError('You should not be here. You are either checking winning numbers or my numbers.')
                    curr_num = []
        # get the leftover curr_num if there is any
        occurrences = 0
        for num in my_numbers:
            if num in winning_numbers:
                occurrences += 1

        if occurrences >= 1:
            total += 2**(occurrences-1)
        else:
            total += 0

    return total

def part_2(data):
    total = 0
    nb_of_cards = len(data) * [1]
    for i in range(len(data)):
        line = data[i]
        my_numbers = []
        curr_num = []
        winning_numbers = set()
        counting_winning_numbers = False
        counting_my_numbers = False
        for char_idx in range(len(line)):
            c = line[char_idx]
            if c != ':' and not counting_winning_numbers and not counting_my_numbers:
                continue
            elif c == ':':
                counting_winning_numbers = True
                continue
            elif c == '|':
                counting_winning_numbers = False
                counting_my_numbers = True
                continue
            else:
                if c.isdigit():
                    curr_num.append(c)
                if (c == ' ' or char_idx==len(line)-1) and len(curr_num) > 0:
                    if counting_winning_numbers:
                        winning_numbers.add(int(''.join(curr_num)))
                    elif counting_my_numbers:
                        my_numbers.append(int(''.join(curr_num)))
                    else:
                        raise ValueError('You should not be here. You are either checking winning numbers or my numbers.')
                    curr_num = []
        # get the leftover curr_num if there is any
        occurrences = 0
        for num in my_numbers:
            if num in winning_numbers:
                occurrences += 1
        for j in range(occurrences):
            if j+i+1 < len(nb_of_cards):
                nb_of_cards[j+i+1] += nb_of_cards[i]
        pass
    return sum(nb_of_cards)

def solve(data):
    print(f"Part_1: {part_1(data)}")
    print(f"Part_2: {part_2(data)}")