"""Parse a linked list from a string"""
class Node:
    """class for node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s: str):
    """from str to linked list"""
    if s == 'None':
        return None
    s = s.split(' -> ')
    head = Node(int(s[-2]))
    s = s[:-2]
    for el in s[::-1]:
        print(el)
        head = Node(int(el),head)
    return head
