def is_unique(test_string):
    seen = {}
    for c in test_string:
        if c in seen:
            return False
        seen[c] = True

    return True


print(is_unique('john'))
print(is_unique('foobar'))
