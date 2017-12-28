from linked_lists import LinkedList, Node, debug


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


last = Node(data='a')
c = Node('c', next=last)
a = Node('a', next=c)
b = Node('b', next=a)
first = Node('a', next=b)
ll = LinkedList(first)

debug(ll)
print('Kth', kth_to_last(ll, k=2).data)
