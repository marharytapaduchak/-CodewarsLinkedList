"""Linked Lists - Move Node"""

class Node(object):
    """class Node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context(object):
    """class Contex"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: "Node", dest: "Node"):
    """func move node"""
    if source is None:
        raise ValueError
    dest = Node(source.data,dest)
    source = Node(source.next.data,source.next.next)
    return Context(source, dest)
