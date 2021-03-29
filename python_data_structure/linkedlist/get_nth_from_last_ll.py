from SingleLinkedList import SingleLinkedList

"""
Q. Give a LinkedList and Integer n , get the nth value, from the Last, of the LL . 
"""


def get_nth(sll, n):
    if len(list(sll)) == n:
        return sll.head.value
    elif len(list(sll)) < n:
        return -1
    else:
        cur = sll.head
        cur_next_n = sll.head
        for i in range(n):
            cur_next_n = cur_next_n.next
        while cur_next_n is not None:
            cur = cur.next
            cur_next_n = cur_next_n.next
        return cur.value


if __name__ == '__main__':
    # Lets create SLL
    ll = [1, 2, 6, 1, 7, 8]
    sll = SingleLinkedList()
    for i in ll:
        sll.insert_start(i)
    print(f'Original LinkedList is {sll}')  # 8->7->1->6->2->1
    print(get_nth(sll, 5))  # 7
