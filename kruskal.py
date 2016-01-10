from undirected_graph import UndirectedGraph
from undirected_graph_examples import graph
from disjoint_set import DisjointSetItem


def kruskal(graph: UndirectedGraph):
    minimum_spanning_tree = []
    set_forest = {}
    
    for node in graph.nodes:
        set_forest[node] = DisjointSetItem(node)
        
    for edge in sorted(graph.edges, key=lambda e: e.weight):
        if set_forest[edge.node1].find() != set_forest[edge.node2].find():
            minimum_spanning_tree.append(edge)
            set_forest[edge.node1].union(set_forest[edge.node2])

    return minimum_spanning_tree


for edge in kruskal(graph):
    print(edge.node1, edge.node2, edge.weight)
