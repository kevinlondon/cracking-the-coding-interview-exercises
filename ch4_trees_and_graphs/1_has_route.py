from collections import deque

class Node:

    def __init__(self, data, neighbors=None):
        self.data = data
        self.neighbors = neighbors if neighbors else []
        self.a_marked = self.b_marked = False


def has_route(a, b):
    a_queue = deque()
    b_queue = deque()

    if a == b:
        return True

    a_queue.append(a); b_queue.append(b)
    while (a_queue or b_queue):
        if a_queue:
            a_node = a_queue.popleft()
            for node in a_node.neighbors:
                if node.b_marked:
                    return True
                elif not node.a_marked:
                    node.a_marked = True
                    a_queue.append(node)

        if b_queue:
            b_node = b_queue.popleft()
            for node in b_node.neighbors:
                if node.a_marked:
                    return True
                elif not node.b_marked:
                    node.b_marked = True
                    b_queue.append(node)

    return False

nodes = [Node(x) for x in range(10)]
nodes[0].neighbors = [nodes[1], nodes[2]]
nodes[2].neighbors = [nodes[1], nodes[4]]
nodes[1].neighbors = [nodes[5]]
nodes[3].neighbors = [nodes[4], nodes[2]]
nodes[4].neighbors = [nodes[1]]
nodes[5].neighbors = [nodes[4]]

print(has_route(nodes[6], nodes[4]))
