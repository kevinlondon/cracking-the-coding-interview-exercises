def sorted_merge(a, b):
    if not b:
        return a

    if not a:
        return b

    a_ptr = 0
    for idx, value in enumerate(a):
        if value is not None:
            a_ptr = idx
        else:
            break

    b_ptr = len(b) - 1
    insert_at = len(a) - 1

    while a_ptr >= 0 or b_ptr >= 0:
        if a_ptr >= 0:
            a_char = a[a_ptr]
        else:
            a_char = None

        if b_ptr >= 0:
            b_char = b[b_ptr]
        else:
            b_char = None

        char = ""
        if a_char is None:
            char = b_char
            b_ptr -= 1
        elif b_char is None:
            char = a_char
            a_ptr -= 1
        elif a_char > b_char:
            char = a_char
            a_ptr -= 1
        else:
            char = b_char
            b_ptr -= 1


        a[insert_at] = char
        insert_at -= 1

    return a


a = [1, 4, 6, 8, None, None, None]
b = [2, 3, 5]

print(sorted_merge(a, b))
