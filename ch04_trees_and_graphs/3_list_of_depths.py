from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = self.next = None

    def __repr__(self):
        return 'Node: {} (Next: {})'.format(self.data, self.next)


def make_linked_lists(root):
    linked_list_roots = []
    tier = deque()
    tier.append(root)

    while tier:
        tier_root, next_tier = build_linked_list(tier)
        linked_list_roots.append(tier_root)
        tier = next_tier

    return linked_list_roots


def build_linked_list(tier):
    next_tier = deque()
    last_node = head = None

    while tier:
        node = tier.popleft()
        if last_node:
            last_node.next = node
        else:
            head = node

        last_node = node

        if node.left:
            next_tier.append(node.left)

        if node.right:
            next_tier.append(node.right)

    return head, next_tier


root = Node(6)
base = Node(1), Node(5)

parent = Node(3)
parent.left = Node(1)
parent.right = Node(5)

root = Node(6)
root.left = parent
root.right = Node(10)

print(make_linked_lists(root))
