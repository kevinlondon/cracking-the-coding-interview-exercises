def count_chars(string):
    chars = {}
    for char in string:
        char = char.lower()
        try:
            chars[char] += 1
        except KeyError:
            chars[char] = 1

    return chars


def is_permutation(a, b):
    if len(a) != len(b):
        return False

    a_chars = count_chars(a)
    b_chars = count_chars(b)
    for character, count in a_chars.items():
        if character not in b_chars or b_chars[character] != count:
            return False

    return True


print(is_permutation('foo', 'ofo'))
print(is_permutation('robert', 'rob'))
print(is_permutation('robert', 'rboter'))
