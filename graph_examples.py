from graph import Graph, Node


nodes = [Node(0), Node(1), Node(2), Node(3),
         Node(4), Node(5), Node(6), Node(7), Node(8)]

nodes[0] \
         .add_neighbour(nodes[3], 2) \
         .add_neighbour(nodes[4], 4)

nodes[1] \
         .add_neighbour(nodes[2], 1) \
         .add_neighbour(nodes[4], 3) \
         .add_neighbour(nodes[5], 7)

nodes[2] \
         .add_neighbour(nodes[1], 1) \
         .add_neighbour(nodes[5], 6)

nodes[3] \
         .add_neighbour(nodes[0], 2)

nodes[4] \
         .add_neighbour(nodes[0], 4) \
         .add_neighbour(nodes[1], 3)

nodes[5] \
         .add_neighbour(nodes[1], 7) \
         .add_neighbour(nodes[2], 6) \
         .add_neighbour(nodes[7], 0) \
         .add_neighbour(nodes[8], 4)

nodes[6] \
         .add_neighbour(nodes[7], 9)

nodes[7] \
         .add_neighbour(nodes[5], 0) \
         .add_neighbour(nodes[6], 9) \
         .add_neighbour(nodes[8], 8)

nodes[8] \
         .add_neighbour(nodes[5], 4) \
         .add_neighbour(nodes[7], 8)

graph = Graph(nodes)
