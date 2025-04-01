"""Linked Lists - Recursive Reverse"""
class Node(object):
    """class for node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def reverse(head):
    """func for reverse"""
    if head is None or head.next is None:
        return head
    temp = reverse(head.next)
    head.next.next = head
    head.next = None
    return temp
