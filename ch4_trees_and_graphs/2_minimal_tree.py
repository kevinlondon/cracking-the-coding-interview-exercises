class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return 'Node: {} (Left: {}, Right: {})'.format(self.data, self.left, self.right)


def make_bst(array, start, end):
    length = end - start
    if length == 0:
        return

    pivot = int((start + end) / 2)
    root = Node(array[pivot])
    if length > 1:
        root.left = make_bst(array, start, pivot)
        root.right = make_bst(array, pivot+1, end)

    return root

array = [1, 3, 5, 6, 8, 10, 11]
root = make_bst(array, 0, len(array))
print(root)
