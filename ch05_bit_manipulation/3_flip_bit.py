def flip_bit(num):
    num = bin(num)
    runs = []; run = 0
    for bit in str(num[2:]):
        if bit == '1':
            run += 1
        else:
            runs.append(run)
            runs.append(0)
            run = 0

    if run:
        runs.append(run)

    longest = 0
    for index, count in enumerate(runs):
        if count == 0:
            if index - 1 > 0:
                lower = runs[index-1]
            else:
                lower = 0

            if index + 1 < len(runs):
                upper = runs[index+1]
            else:
                upper = 0

            count = 1 + upper + lower

        if count > longest:
            longest = count

    return longest


print(flip_bit(1775))
