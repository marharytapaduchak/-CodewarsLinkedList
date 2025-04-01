"""Linked Lists - Remove Duplicates"""

class Node(object):
    """class for node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    """func for remove duplicates"""
    if head is None:
        return None
    if head.next is None:
        return head
    temp = head
    while temp.next is not None:
        if temp.data == temp.next.data:
            if temp.next.next is None:
                temp.next = None
                break
            else:
                temp.next = temp.next.next
        else:
            temp = temp.next
    return head
