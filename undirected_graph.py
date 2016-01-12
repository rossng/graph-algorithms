import random
from typing import Sequence


class Node:
    def __init__(self, key):            
        self.id = key

    def __str__(self):
        return 'Node ' + str(self.id)


class Edge:    
    def __init__(self, node1: Node, node2: Node, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


class UndirectedGraph:
    def __init__(self, nodes: Sequence[Node], edges: Sequence[Edge]):
        self.nodes = nodes
        self.edges = edges

    def get_random_node(self):
        return random.choice(self.nodes)

    def neighbours_of(self, node: Node):
        # Not exactly efficient but it'll do
        node2s = map(lambda e: e.node2, filter(lambda e: e.node1 == node, self.edges))
        node1s = map(lambda e: e.node1, filter(lambda e: e.node2 == node, self.edges))

        return list(node2s) + list(node1s)

    def get_edge_between(self, node1: Node, node2: Node):
        matching_edges = list(filter(lambda e: (e.node1 == node1 and e.node2 == node2) or (e.node2 == node1 and e.node1 == node2),
                      self.edges))
        return matching_edges[0] if matching_edges else None