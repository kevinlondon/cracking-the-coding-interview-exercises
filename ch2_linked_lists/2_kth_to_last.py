def kth_to_last(linked_list, k):
    lead = 0
    head = linked_list.head
    trailing = linked_list.head

    while head != None:
        head = head.next
        if lead == k:
            trailing = trailing.next
        else:
            lead += 1

    if lead != k:
        return None
    else:
        return trailing


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
print('Kth', kth_to_last(ll, k=2).data)
