def remove_dups(linked_list):
    seen = {}
    last_node = None
    node = linked_list.head
    while node != None:
        validate_unique(node)
        node = node.next


def validate_unique(node):
    search_node = node.next
    last_seen = node
    while search_node != None:
        if search_node.data == node.data:
            last_seen.next = search_node.next
        else:
            last_seen = search_node

        search_node = search_node.next


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


last = Node(data='a')
c = Node('c', next=last)
a = Node('a', next=c)
b = Node('b', next=a)
first = Node('a', next=b)
ll = LinkedList(first)

debug(ll)
remove_dups(ll)
debug(ll)
