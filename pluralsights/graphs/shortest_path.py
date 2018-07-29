#!/usr/bin/env python

'''
This file implements the shortest_path algorithm for finding the
shortest path between two vertices in a graph. 

shortest_path algorithm is most commonly used for finding the
path with minimum hops between two nodes in a unweighted graph.
For weighted graphs, Djikstra's algorithm is used
'''

''' 
Key Datastructures:
1. Distance Table: A table which contains 1 row for each node in 
the graph and with 3 columns:
    a. Name: Node name
    b. Distance: Distance from the source node
    c. Preceding Node: Last node encountered along the shorted path

Most efficient way to store a distance table is to maintain a hashmap
with key = node and value = (distance, preceding_node). This offers
constant time lookup

2. Stack: Used to bracktrack and determine the shortest path once
the distance table is created. Might be possible to user recursion 
here
'''

from Queue import Queue
from pluralsights.graphs import AdjacencySetGraph
from ds.Stack import Stack

def build_distance_table(g, src):
    distance_table = {}
    for i in range(g.num_vertices):
        distance_table[i] = (-1, None)

    distance_table[src] = (0, src)

    # Initialize the queue and add the source node to it
    q = Queue()
    q.put(src)

    visited = []

    # Loop through each node and it's adjacencies and update
    # the distance table, starting at the src node
    while not q.empty():
        v = q.get()

        if v in visited:
            continue

        # Mark the current node as visited
        visited.append(v)

        print "PROCESSING vertex", v , "from Queue..."
        print "DT:", distance_table
        for node in g.get_adjacent_vertices(v):
            print "Processing node:", node, "for vertex", v
            # Update the distance table
            if node not in visited:
                distance_table[node] = (1+distance_table[v][0], v)
                q.put(node)
                print "Updated and added", node, "to queue.."

    return distance_table

def shortest_path(g, src, dst):
    distance_table = build_distance_table(g, src)

    print "Distance Table:", distance_table

    # Now to find the shortest path, we backtrack from dst node, until
    # we reach src node
    path = [dst]

    previous_vertex = distance_table[dst][1]

    while previous_vertex is not None and previous_vertex is not src:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
        
    if previous_vertex is None:
        raise ValueError("There it not path from", src, "to", dst)

    path = [src] + path
    return path

if __name__ == "__main__":
    g = AdjacencySetGraph(4, directed=True)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    '''
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(0, 7)
    '''

    res = shortest_path(g, 0, 3)
    print "Shorted path:", res
    #print "Shorted path:", shortest_path(g, 0, 6)
    #print "Shorted path:", shortest_path(g, 7, 4)
