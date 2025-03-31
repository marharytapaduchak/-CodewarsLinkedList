"""Linked Lists - Push & BuildOneTwoThree"""
from preloaded import Node

def push(head, data):
    """func for pushing data to list"""
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """func for building one-two-three"""
    return push(push(Node(3),2),1)
