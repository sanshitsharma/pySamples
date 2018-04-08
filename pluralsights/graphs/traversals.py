#!/usr/bin/python

from Queue import Queue
from pluralsights.graphs import AdjacencyMatrixGraph
from ds.Stack import Stack

# Prints breadth first traversal of the graph starting at 
# the specified node
def breadth_first(g, start):
    # Create a queue and add the start node to queue
    q = Queue()
    q.put(start)

    # Create a list which will keep track of all nodes that 
    # have been visited
    visited = []

    while not q.empty():
        # Get a vertex from the front of the queue
        v = q.get()

        # If vertex is already visited, nothing to do here
        if v in visited:
            continue

        # Print the unvisited node
        print "Visit:", v
        visited.append(v)

        # Add all 1-hop neighbors to queue
        for node in g.get_adjacent_vertices(v):
            if node not in visited:
                q.put(node)

# Prints depth first traversal of the graph starting at 
# the specified node. Logic is same as breadth first but
# instead of using queue need a stack so this function 
# can be written recursively
def depth_first(g, visited, current=0):
    if current in visited:
        return

    print "Visit:", current
    visited.append(current)

    for node in g.get_adjacent_vertices(current):
            depth_first(g, visited, node)

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(9, directed=True)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 4)
    g.add_edge(6, 8)

    print "************** BFT ************** "
    breadth_first(g, 0)

    print "\n************** DFT ************** "
    visited = []
    depth_first(g, visited)