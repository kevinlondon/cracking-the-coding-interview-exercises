def conversion(a, b):
    return bin(a^b).count('1')

print(conversion(0, 15))
