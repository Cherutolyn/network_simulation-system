from node import Node

# Create nodes
A = Node("A")
B = Node("B")
C = Node("C")

# Connect nodes
A.connect(B)
B.connect(C)

# Print connections
print(A.name, "connected to:", [node.name for node in A.connections])
print(B.name, "connected to:", [node.name for node in B.connections])