"""Swap Node Pairs In Linked List"""
class Node:
    """class for node"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """func for swaping pairs"""
    if head is None or head.next is None:
        return head
    res = Node()
    res.next = head
    temp = res

    while temp.next and temp.next.next:
        first = temp.next
        second = temp.next.next
        first.next = second.next
        second.next = first
        temp.next = second

        temp = first

    return res.next
