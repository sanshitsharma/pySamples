#/usr/bin/env python

from ds.graph.graphs import AdjacencySetGraph

# breadth_first_search searches for a path between src and 
# dst nodes. 
def breadth_first_search(g, src, dst):
    if not g or not src or not dst:
        return None

    start = g.get_vertex(src)
    if not start:
        return None

    # Set the properties for start
    start.color = 'White'
    start.pred = None
    start.dist = 0

    end = g.get_vertex(dst)
    if not end:
        return None

    # A queue to keep track of vertices next in line to be visited
    vertQ = [start]
    dst_found = False

    while vertQ:
        curr = vertQ.pop(0)
        # Change color for start
        curr.color = 'Gray'
        for nbr in curr.get_neighbors():
            if nbr.color == 'White':
                nbr.color = 'Gray'
                nbr.pred = curr
                nbr.dist = curr.dist + 1
                vertQ.append(nbr)

            if nbr == end:
                dst_found = True
                break
        curr.color = 'Black'
        if dst_found:
            break

    if not dst_found:
        print "No path found from", src, "to", dst
        return None

    # Now start at from dst and trace back the route to src
    curr = end
    path = []
    while curr.pred:
        path = [curr.id] + path
        curr = curr.pred
    path = [curr.id] + path

    # Finally reset the bfs properties of all vertices
    for v in g:
        v._reset_search_properties()

    return path