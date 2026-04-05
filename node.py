class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, other_node):
        if other_node not in self.connections:
            self.connections.append(other_node)
            other_node.connections.append(self)

    def __str__(self):
        return f"Node({self.name})"