from linked_lists import LinkedList, Node, debug


def remove_dups(linked_list):
    seen = {}
    last_node = None
    node = linked_list.head
    while node != None:
        if node.data in seen:
            last_node.next = node.next
        else:
            seen[node.data] = True
            last_node = node

        node = node.next

    return linked_list


last = Node(data='a')
c = Node('c', next=last)
a = Node('a', next=c)
b = Node('b', next=a)
first = Node('a', next=b)
ll = LinkedList(first)

debug(ll)
remove_dups(ll)
debug(ll)
