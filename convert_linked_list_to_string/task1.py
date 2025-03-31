"""Convert a linked list to a string"""
class Node():
    """class for node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node) -> str:
    """write list"""
    if node is None:
        return 'None'
    res = ''
    while node.next is not None:
        res += f'{node.data} -> '
        node = node.next
    return res + f'{node.data} -> '+ 'None'


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
