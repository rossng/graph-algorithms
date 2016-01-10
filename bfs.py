from graph_examples import graph
from queue import Queue

def breadth_first_search(root):

    distances = {}
    parents = {}
    q = Queue()

    distances[root] = 0
    parents[root] = None
    q.put(root)

    while not q.empty():
        
        current_node = q.get()

        for neighbour in current_node.get_neighbours():
            if not neighbour in distances:
                distances[neighbour] = distances[current_node] + 1
                parents[neighbour] = current_node
                q.put(neighbour)
                
    return (distances, parents)

root = graph.get_random_node()

(distances, parents) = breadth_first_search(root)

[print(n.id, d) for (n, d) in sorted(distances.items(), key=lambda i: i[0].id)]
