from SingleLinkedList import SingleLinkedList

"""
Q. Given a LinkedList having Duplicate Integers , remove the Duplicate elements from the LL.
"""


def remove_duplicate(sll):
    visited = []
    cur = sll.head
    while cur is not None:
        visited.append(cur.value)
        if cur.next.value in visited:
            duplicate = cur.next
            cur.next = duplicate.next
            duplicate.next = None
        cur = cur.next


if __name__ == '__main__':
    """
    Original LinkedList is 8->7->1->6->2->1
    Duplicate removed LinkedList is 8->7->1->6->2
    """
    # Lets create SLL
    ll = [1, 2, 6, 1, 7, 8]
    sll = SingleLinkedList()
    for i in ll:
        sll.insert_start(i)
    print(f'Original LinkedList is {sll}')
    remove_duplicate(sll)
    print(f'Duplicate removed LinkedList is {sll}')
