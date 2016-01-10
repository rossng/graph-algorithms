from undirected_graph import UndirectedGraph, Node, Edge


nodes = [Node(0), Node(1), Node(2), Node(3),
         Node(4), Node(5), Node(6), Node(7), Node(8)]

edges = [ \
    Edge(nodes[0], nodes[3], 2), \
    Edge(nodes[0], nodes[4], 4), \
    Edge(nodes[4], nodes[1], 3), \
    Edge(nodes[1], nodes[2], 1), \
    Edge(nodes[1], nodes[5], 7), \
    Edge(nodes[2], nodes[5], 6), \
    Edge(nodes[5], nodes[8], 4), \
    Edge(nodes[5], nodes[7], 0), \
    Edge(nodes[8], nodes[7], 8), \
    Edge(nodes[7], nodes[6], 9)]

graph = UndirectedGraph(nodes, edges)
