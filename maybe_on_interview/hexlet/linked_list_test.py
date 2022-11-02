from maybe_on_interview.hexlet.linked_list import Node

def test_is_circular1():
    last = Node(8)
    head = Node(7, last)
    head = Node(6, head)
    assert not head.is_circular()

def test_is_circular2():
    last = Node(8)
    head = Node(7, last)
    head = Node(6, head)
    head = Node(5, head)
    head = Node(4, head)
    head = Node(3, head)
    head = Node(2, head)
    head = Node(1, head)
    last.next_node = head
    assert head.is_circular()


print(test_is_circular1())
print(test_is_circular2())