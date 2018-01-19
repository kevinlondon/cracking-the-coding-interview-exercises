def delete_middle(linked_list, to_delete):
    advance_node = linked_list.head.next
    trailing_node = linked_list.head

    while advance_node != to_delete and advance_node:
        advance_node = advance_node.next
        trailing_node = trailing_node.next

    if advance_node == to_delete:
        trailing_node.next = to_delete.next

    return linked_list


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
delete_middle(ll, to_delete=b)
print('Removed', debug(ll))
