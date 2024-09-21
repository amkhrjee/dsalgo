class Node:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __hash__(self):
        return hash(self.data)


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.nodes_count = len(nodes)
        self.adjacency_list = {node: set() for node in nodes}

    def connect(self, node_one: Node, node_two: Node):
        self.adjacency_list[node_one].add(node_two)
        self.adjacency_list[node_two].add(node_one)

    def neighbors(self, node):
        return [each_node for each_node in self.adjacency_list[node]]
