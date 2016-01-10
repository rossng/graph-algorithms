from graph_examples import graph

def depth_first_search(root):

    distances = {}
    parents = {}
    stack = []

    distances[root] = 0
    parents[root] = None
    stack.append(root)

    while stack:
        
        current_node = stack.pop()

        for neighbour in current_node.get_neighbours():
            if not neighbour in distances:
                distances[neighbour] = distances[current_node] + 1
                parents[neighbour] = current_node
                stack.append(neighbour)
                
    return (distances, parents)

root = graph.get_random_node()

(distances, parents) = depth_first_search(root)

[print(n.id, d) for (n, d) in sorted(distances.items(), key=lambda i: i[0].id)]
