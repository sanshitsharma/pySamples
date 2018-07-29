#!/usr/bin/env python

from ds.graph import AdjacencySetGraph as Graph
from ds.graph.traversals import breadth_first_search as bfs 

def main():
    g = Graph()
    g.add_vertex('hit')
    g.add_vertex('hot')
    g.add_vertex('dot')
    g.add_vertex('log')
    g.add_vertex('dog')
    g.add_vertex('lot')
    g.add_vertex('cog')

    g.add_edge('hit', 'hot')
    g.add_edge('hot', 'dot')
    g.add_edge('dot', 'dog')
    g.add_edge('hot', 'lot')
    g.add_edge('dot', 'lot')
    g.add_edge('dog', 'log')
    g.add_edge('dog', 'cog')
    g.add_edge('log', 'cog')
    g.add_edge('lot', 'log')

    for vertex in g:
        for nbr in vertex.get_neighbors():
            print("(%s, %s)" % (vertex.id, nbr.id))

    #print g.dfTrav()
    print bfs(g, 'hit', 'cog')

if __name__ == "__main__":
    main()