class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def is_circular(self): #is there circle?
        first = self.value
        while self:
            if self.next_node == None:
                # print('fl')
                return False
            if self.next_node.value == first:
                # print('tr')
                return True
            self = self.next_node

    # BEGIN resheie uchitelya
    # def is_circular(self):
    #     # BEGIN
    #     slow = self
    #     fast = self
    #
    #     while fast:
    #         slow = slow.next_node
    #         fast = fast.next_node
    #         if fast:
    #             fast = fast.next_node
    #             if slow is fast:
    #                 return True
    #
    #     return False
   # END

    def print_list(head, end='\n'):
        first = head.value
        print(first,'mk')
        while head:
            # print(head.value, end=' -> ' if head.next_node else '')
            if head.next_node.value == first:
                break
            head = head.next_node
            print(head.next_node.value)
        # print(end=end)