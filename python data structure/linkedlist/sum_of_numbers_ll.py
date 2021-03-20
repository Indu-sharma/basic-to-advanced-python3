"""
You are given two Numbers and each is represented by LinkedLists where single digit is stored in a node.
The Numbers are stored in LL in reverse order. Find the Sum of Two numbers as LL.
Ex -
n1 = 789 , ll1 = 9->8->7
n2 = 211 , ll2 = 1->1->2

OutPut:
sum = 1000, ll = 0->0->0->1

"""
from SingleLinkedList import SingleLinkedList


def split_digits(n):
    if n > 9:
        yield n % 10
        yield from split_digits(n // 10)
    else:
        yield n


def sum_ll(ll1, ll2):
    ll3 = SingleLinkedList()
    cur1 = ll1.head
    cur2 = ll2.head
    cary = 0
    while cur1 is not None and cur2 is not None:
        sum_ = cur1.value + cur2.value + cary
        res = sum_ % 10
        ll3.insert_end(res)
        cary = sum_ // 10
        cur1 = cur1.next
        cur2 = cur2.next
    ll3.insert_end(cary)
    return ll3


if __name__ == '__main__':
    # Lets create Linked Lists for n1 = 789 & n2 = 211
    n1 = 789
    n2 = 211
    ll1 = SingleLinkedList()
    ll2 = SingleLinkedList()
    for i in split_digits(n1):
        ll1.insert_end(i)
    for i in split_digits(n2):
        ll2.insert_end(i)
    print(ll1)  # 9->8->7
    print(ll2)  # 1->1->2
    ll3 = sum_ll(ll1, ll2)
    print(ll3) # 0->0->0->1
