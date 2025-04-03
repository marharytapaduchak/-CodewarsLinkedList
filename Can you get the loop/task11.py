"""Can you get the loop ?"""
def loop_size(node):
    """func to count loop size"""
    normal, double = node, node

    while double and double.next:
        normal = normal.next
        double = double.next.next
        if normal == double:
            break

    cnt = 1
    temp = normal.next
    while temp != normal:
        cnt += 1
        temp = temp.next
    return cnt
