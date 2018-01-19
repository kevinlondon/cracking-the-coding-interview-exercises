def insertion(m, n, i, j):
    upper_mask = (-1 << (j+1))
    lower_mask = (1 << i) - 1
    masked_n = (upper_mask & n) | (lower_mask & n)
    return bin(masked_n | (m << i))

n = 0b100000000000
m = 0b10011
i = 2
j = 6
print(insertion(m, n, i, j))
