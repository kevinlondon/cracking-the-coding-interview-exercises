def is_unique(test_string):
    last_seen = ""
    test_string = sorted(test_string)

    for c in test_string:
        c = c.lower()
        if c == last_seen:
            return False
        else:
            last_seen = c

    return True

print(is_unique('john'))
print(is_unique('fobor'))
