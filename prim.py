from min_heap import MinHeap
from undirected_graph import UndirectedGraph
from undirected_graph_examples import graph


def set_node_distance(node, distance):
    node.distance = distance


def prim(graph: UndirectedGraph):
    for node in graph.nodes:
        node.distance = None
        node.parent = None
        node.in_queue = True

    graph.nodes[0].distance = 0
    q = MinHeap(graph.nodes, lambda n: n.distance, set_node_distance)

    while q.get_min():
        u = q.pop_min()
        u.in_queue = False
        for v in graph.neighbours_of(u):
            uv_edge = graph.get_edge_between(u, v).weight
            if v.in_queue and uv_edge < v.distance:
                v.parent = u
                v.distance = uv_edge.weight


prim(graph)
