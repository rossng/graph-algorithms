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
        return filter(
            lambda edge: edge.node1 == node or edge.node2 == node,
            self.edges)
