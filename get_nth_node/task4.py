"""Linked Lists - Get Nth Node"""
# from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """func get_nth"""
    if node is None:
        raise ValueError("None linked list should throw error.")
    if index < 0:
        raise IndexError
    for _ in range(index):
        if node.next is None:
            raise IndexError("Invalid index value should throw error.")
        node = node.next
    return node
