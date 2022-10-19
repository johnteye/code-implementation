# all string are truety values except the empty strings
# numbers are truety values except 0
# objects are true expect None/Null

### Linked lists implementation
# A -> B -> C ->
'''
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
'''

class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next

node_1 = Node("Once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

node_2.next_node = node_3
node_1.next_node = node_2
node_3.next_node = node_4 


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index +=1
            return current_node.val 
        
list1 = LinkedList(node_1)

print(list1.read(2))