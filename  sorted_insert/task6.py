"""Linked Lists - Sorted Insert"""
class Node(object):
    """class Node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    """func sorted_insert"""
    temp = Node(data)
    if head is None:
        return temp
    if data < head.data:
        temp.next = head
        return temp

    node = head
    while node.next is not None and node.next.data < data:
        node = node.next

    temp.next = node.next
    node.next = temp
    return head
