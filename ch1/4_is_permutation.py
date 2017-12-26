from collections import defaultdict


def is_palindrome_permutation(string):
    chars = defaultdict(int)
    length = 0
    for char in string:
        if char == " ":
            continue

        char = char.lower()
        chars[char] += 1
        length += 1

    is_even = (length % 2 == 0)
    found_odd = False

    for char, count in chars.items():
        if count % 2 != 0:
            if is_even:
                return False
            elif found_odd:
                return False
            else:
                found_odd = True

    return True


print(is_palindrome_permutation('Tact coa'))
print(is_palindrome_permutation('Tac coa'))
print(is_palindrome_permutation('Tact ca'))
