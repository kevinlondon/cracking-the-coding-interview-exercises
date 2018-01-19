def rotated_search(array, needle):
    if not array:
        return None

    mid = int(len(array) / 2)
    mid_val = array[mid]

    if mid_val == needle:
        return mid

    right_val = array[-1]
    if (needle > mid_val and not needle > right_val) or (needle < mid_val and needle < array[0]):
        return rotated_search(array[mid+1:], needle) + 1 + mid
    else:
        return rotated_search(array[:mid], needle)


print(rotated_search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))
