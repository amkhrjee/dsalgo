from graph import Graph, Node


def bfs(g: Graph, start_node: Node, data: int):
    q = [start_node]
    visited = []

    while len(q) > 0:
        curr_node = q.pop()
        if curr_node.data == data:
            return True
        visited.append(curr_node)
        q += [node for node in g.neighbors(curr_node) if node not in visited]
    return False


def test_():
    A = Node(10)
    B = Node(9)
    C = Node(1)
    D = Node(12)
    E = Node(3)
    F = Node(4)
    g = Graph([A, B, C, D, E, F])
    g.connect(A, B)
    g.connect(A, C)
    g.connect(C, D)
    g.connect(B, D)
    g.connect(D, E)
    g.connect(E, F)

    assert bfs(g, A, 12)
