# all string are truety values except the empty strings
# numbers are truety values except 0
# objects are true expect None/Null

### Linked lists implementation
# A -> B -> C ->

from platform import node


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')


node_a.next = node_b
node_b.next = node_c
        
node = node_a
while node:
    print(node.val)
    node = node.next