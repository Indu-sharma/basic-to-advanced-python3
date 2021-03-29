from SingleLinkedList import SingleLinkedList

"""
Q. Given a LinkedList of Integers and a value x ; partition the LL such that:
 Integers < x are on left side of LL and Integers >= x are on the right side of LL.
"""


def partition(sll, x):
    new_sll = SingleLinkedList()
    cur = sll.head
    while cur is not None:
        if cur.value < x:
            new_sll.insert_start(cur.value)
        else:
            new_sll.insert_end(cur.value)
        cur = cur.next
    return new_sll


if __name__ == '__main__':
    """
    OutPut:
    Original LinkedList is 8->7->1->6->2->1
    Partitioned linkedList around 6 is:1->2->1->8->7->6 
    """
    # Lets create SLL
    ll = [1, 2, 6, 1, 7, 8]
    sll = SingleLinkedList()
    for i in ll:
        sll.insert_start(i)
    print(f'Original LinkedList is {sll}')  # 8->7->1->6->2->1
    partition_value = 6
    new_ssl = partition(sll, partition_value)
    print(f'Partitioned linkedList around {partition_value} is:{new_ssl} ')
