import random

class Graph:
    nodes = []

    def __init__(self, nodes):
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def get_random_node(self):
        return random.choice(self.nodes)

    def get_edge_tuples(self):
        for node in self.nodes:
            for neighbour, weight in node.get_edges():
                yield (node, neighbour, weight)


class Node:
    def __init__(self, key, neighbours=None):
        if neighbours is None:
            neighbours = {}
            
        self.id = key
        self.neighbours = neighbours

    def add_neighbour(self, neighbour, weight=0):
        self.neighbours[neighbour] = weight
        return self

    def __str__(self):
        return 'Node ' + str(self.id) + \
               ' [' + " ".join(['N' + str(x.id) + ':w' + str(self.neighbours[x]) \
                for x in self.neighbours]) + ']'

    def get_edges(self):
        return self.neighbours.items()

    def get_neighbours(self):
        return self.neighbours.keys()

    def get_edge(self, neighbour):
        return self.neighbours.get(neighbour)

    def get_id(self):
        return self.id
