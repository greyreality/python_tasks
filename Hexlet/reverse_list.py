"""Reverse linked list."""
class Node: #  """Linked list is either None or a value and a link to the next list."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
head = Node(1, Node(2, Node(3, Node(4))))

def print_list(head, end='\n'):
    while head:
        print(head.value, end=' -> ' if head.next else '')
        # print('next=',head.next)
        head = head.next
    print('\t')
print_list(head)
def reverse_list(head, tail=None):
    while head is not None:
        # head = head.next
        # tail = head
        # head.next = tail
        head.next, tail, head = tail, head, head.next
        # print(head)
    return tail
print('reverse=')
print_list(reverse_list(head))