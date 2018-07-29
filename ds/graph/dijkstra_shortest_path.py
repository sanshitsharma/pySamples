#!/usr/bin/python

from ds.graph import AdjacencySetGraph, Vertex
from ds.PriorityQueue import PriorityQueue
import sys

"""
The idea of dijkstra's algorithm is to find the shortest path between
two nodes of a graph
"""

def dijkstras_shortest_path(g, src, dst):
    start = g.get_vertex(src)
    end = g.get_vertex(dst)

    if not start or not end:
        return 0, None

    # Set distances for all nodes to sys.maxint
    for v in g:
        if v == start: # distance for start node needs to be 0
            v.set_distance(0)
        else:
            v.set_distance(sys.maxint)

    # Use a priority queue to create a min heap of the nodes based on there
    # dist values and key as the vertex itself
    pq = PriorityQueue()
    for v in g:
        pq.add(v.get_distance(), v)

    # Iterate while pq is not empty
    while not pq.is_empty():
        vertex = pq.remove()[1]
        #print "Evaluating vertex:", str(vertex), "type:", type(vertex)
        vertex.color = 'Black'
        for nbr in vertex.get_neighbors():
            #print "Checking neighbor:", str(nbr), "type:", type(nbr)
            if nbr.color == 'White':
                newDist = vertex.get_distance() + g.get_edge_weight(vertex.id, nbr.id)
                if newDist < nbr.get_distance():
                    nbr.set_distance(newDist)
                    nbr.set_predecessor(vertex)
                    pq.updateKey(nbr, newDist)

        # Print the updated pq
        '''
        print "Post evaluation of vertex:", vertex.id
        for item in pq:
            ans = 'Priority = ' + str(item[0]) + ' Vertex: ' + item[1].id
            if item[0] != sys.maxint:
                ans += ' Pred: ' + item[1].get_predecessor().id
            print ans
        print
        '''

    dist = end.get_distance()
    path = [end.id]
    pred = end.get_predecessor()
    while pred:
        path = [pred.id] + path
        end = pred
        pred = end.get_predecessor()

    return dist, path

if __name__ == "__main__":
    g = AdjacencySetGraph()
    g.add_edge('1.1', '1.2', w=1)
    g.add_edge('1.2', '1.3', w=1)
    g.add_edge('1.3', '1.4', w=1)
    g.add_edge('1.4', '1.5', w=1)
    g.add_edge('1.1', '1.4', w=1)

    #g.display()
    print dijkstras_shortest_path(g, '1.1', '1.5')