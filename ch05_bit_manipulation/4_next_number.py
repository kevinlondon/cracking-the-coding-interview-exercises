def next_number(num):
    if num == 0:
        return

    ones = count_ones(num)
    next_num = num + 1
    while count_ones(next_num) != ones and next_num > 0:
        next_num += 1

    lower_num = num - 1
    while count_ones(lower_num) != ones and lower_num > 0:
        lower_num -= 1

    return lower_num, next_num


def count_ones(num):
    return bin(num).count('1')


print(next_number(50))
