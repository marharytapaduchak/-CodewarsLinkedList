"""Linked Lists - Alternating Split"""
class Node(object):
    """class for node"""
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Context(object):
    """class for context"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """func for alternating split"""
    if head is None or head.next is None:
        raise ValueError
    first_ = head
    second_ = head.next

    first = first_
    second = second_

    while first and first.next and second and second.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next

    first.next = None
    return Context(first_, second_)
