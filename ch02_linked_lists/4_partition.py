from linked_lists import LinkedList, Node, debug

def partition(linked_list, x):
    first_low = first_high = low_tail = high_tail = None
    node = linked_list.head

    while node != None:
        next = node.next
        node.next = None

        if node.data < x:
            if low_tail:
                low_tail.next = node
            else:
                first_low = node

            low_tail = node
        else:
            if high_tail:
                high_tail.next = node
            else:
                first_high = node

            high_tail = node

        node = next

    low_tail.next = first_high
    return LinkedList(first_low)

last = Node(data=1)
c = Node(2, next=last)
a = Node(10, next=c)
b = Node(5, next=a)
first = Node(8, next=b)
ll = LinkedList(first)

debug(ll)
print('partition', debug(partition(ll, 5)))
