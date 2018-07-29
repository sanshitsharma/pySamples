#!/usr/bin/python

'''
Topological sort applies to a directed graph. It is most frequently used in DAGs.
DAG's models precedence relationship where one node is precededed by one or more
nodes except for the start node. 
A topological sort is any ordering of all the vertices of the graph that satisfies
all precedence relationships.
'''

from Queue import Queue
from pluralsights.graphs import AdjacencyMatrixGraph

# topological_sort funtion returns an ordering of nodes which satisfy the indegree
# precedence. If a cycle exists in grpah, a ValueError is raised
def topological_sort(g):
    # We create a queue to keep a track of all nodes whose precedence count = 0
    q = Queue()

    # We also maintain a mop which tracks the current precedence values of all
    # vertices in the graph. 
    precedence_map = {}

    # Initialize the map with the precedence values of the vertices at the beginning.
    # The preceence value of a node is the indegree of the node
    for i in range(g.num_vertices):
        precedence_map[i] = g.get_indegree(i)

        # If indegree of vertex is 0, add it to the queue
        if precedence_map[i] == 0:
            q.put(i)

    result = []
    # Loop until queue has some values
    while not q.empty():
        # Get node from queue
        vertex = q.get()

        # Add node to result
        result.append(vertex)

        # Once this vertex is processed, it's logically removed from the 
        # graph so we decreament the precedence count for all it's 
        # adjacencies
        for node in g.get_adjacent_vertices(vertex):
            precedence_map[node] -= 1
            if precedence_map[node] == 0:
                q.put(node)

    # Once we have processed all the nodes we check to see it the lenght of result
    # is equal to num of vertices in out graph. If that's not the case, we raise
    # a ValueError
    if len(result) != g.num_vertices:
        raise ValueError("Graph has a cycle. Topological sort is NOT possible")

    return result

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(9, directed=True)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(3, 4)
    g.add_edge(6, 8)

    print topological_sort(g)
