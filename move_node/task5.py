"""Linked Lists - Move Node"""

class Node(object):
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """class Contex"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """func move node"""
    # Your code goes here.
    # Remember to return the context.
    return Context(source, dest)
