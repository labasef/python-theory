class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create two nodes
node1 = Node(1)
node2 = Node(2)

# Create circular references
# node1 references node2
# node2 references node1
node1.next = node2
node2.next = node1


