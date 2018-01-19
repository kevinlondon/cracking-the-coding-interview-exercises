def sorted_search(array, needle, left=0, right=1):
    l_num = array.elementAt(left)
    r_num = array.elementAt(right)
    if l_num == needle:
        return left
    elif r_num == needle:
        return right

    diff = right - left

    if r_num < needle and r_num != -1:
        return sorted_search(array, needle, right, right + (diff * 2))
    elif l_num > needle:
        return sorted_search(array, needle, left - (diff * 2), left)
    else:
        return sorted_search(array, needle, left + int(diff / 2), right)


class Array:

    def __init__(self, array):
        self.array = array

    def elementAt(self, index):
        if index > len(self.array) - 1:
            return -1

        return self.array[index]


array = Array([0, 1, 2, 3, 5, 6, 10, 18])
print(sorted_search(array, needle=6))
