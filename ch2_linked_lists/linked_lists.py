class LinkedList:
    def __init__(self, head):
        self.head = head


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def debug(linked_list):
    node = linked_list.head
    print('Debugging')
    while node != None:
        print(node.data)
        node = node.next


