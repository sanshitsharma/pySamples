#!/usr/bin/env python

import abc 

######################################################################
# Graph is an abstract class that defines the interface for any graph 
# implmentation that we will do
######################################################################
class Graph(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, directed=False):
        self.num_vertices = 0
        self.directed = directed

    @abc.abstractmethod
    def add_vertex(self, v):
        pass

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight=0):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

#######################################################################
#
# An adjacency set/list representation of graph requires a Vertex class
# which represents a node in the graph. Each node stores the ID. The
# adjacent neighbor information as a dictionary where the key is the 
# neighbor node and the value is the weight of the edge between the two
# nodes. 
#
# The AdjacencySetGraph class will keep a count of the total nodes and
# an array of the nodes
#
#######################################################################
class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.neighbors = {}
        # Additional properties that will be used in breadth first search
        self.pred = None
        self.color = 'White'
        self.dist = 0

    def _reset_search_properties(self):
        self.pred = None
        self.color = 'White'
        self.dist = 0

    def __str__(self):
        return "Vertex: " + str(self.id) + " Dist: " + str(self.dist) + " Color: " + self.color + ' connectedTo: ' + str([x.id for x in self.neighbors])

    def add_neighbor(self, nbr, weight=0):
        self.neighbors[nbr] = weight
    
    def get_neighbors(self):
        return self.neighbors.keys()

    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def set_distance(self, val):
        self.dist = val

    def get_distance(self):
        return self.dist

    def set_predecessor(self, v):
        self.pred = v

    def get_predecessor(self):
        return self.pred

class AdjacencySetGraph(Graph):
    def __init__(self, directed=False):
        #super(AdjacencySetGraph, self).__init__(directed)
        self.num_vertices = 0
        self.directed = directed
        self.vertices = {}

    def __contains__(self, n):
        return n in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, v):
        self.num_vertices += 1
        node = Vertex(v)
        self.vertices[v] = node
        return node

    def add_edge(self, v1, v2, w=0):
        if v1 not in self.vertices.keys():
            self.num_vertices += 1
            node1 = Vertex(v1)
            self.vertices[v1] = node1
        if v2 not in self.vertices.keys():
            self.num_vertices += 1
            node2 = Vertex(v2)
            self.vertices[v2] = node2

        # Add the edge from v1 to v2
        self.vertices[v1].add_neighbor(self.vertices[v2], w)
        if not self.directed:
            self.vertices[v2].add_neighbor(self.vertices[v1], w)

    def get_vertex(self, v):
        try:
            return self.vertices[v]
        except KeyError as ke:
            return None

    def get_adjacent_vertices(self, v):
        if v not in self.vertices.keys():
            return None
        return v.get_neighbors()

    def get_indegree(self, v):
        indegree = 0
        for key, node in self.vertices.iteritems():
            if v in node.get_neighbors():
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            return None
        
        return self.vertices[v1].get_weight(self.vertices[v2])

    def display(self):
        for k, v in self.vertices.iteritems():
            print "Node", k, "-->", v.get_neighbors()

    '''
    def __printStk(self, stk):
        return [x.id for x in stk]
    '''

    # Return the path between vertex v1 and v2 is both exist in the
    # graph
    def dft(self):
        if not self.vertices:
            return []

        stk = [self.vertices[self.vertices.keys()[0]]]
        ans = []
        visited = {}

        while stk:
            #print "Stk:", self.__printStk(stk)
            curr = stk.pop()
            ans.append(curr.id)
            visited[curr] = 1
            nbrs = curr.get_neighbors()
            for nbr in nbrs:
                try:
                    visited[nbr]
                except KeyError as ke:
                    if nbr not in stk:
                        stk.append(nbr)
        return ans

    def df_trav(self):
        curr = self.vertices[self.vertices.keys()[0]]
        visited = []

        self._df_trav_util(curr, visited)
        return [x.id for x in visited]

    def _df_trav_util(self, curr, visited):
        if curr in visited:
            return

        visited.append(curr)
        for nbr in curr.get_neighbors():
            self._df_trav_util(nbr, visited)


if __name__ == "__main__":
    g = AdjacencySetGraph(directed=True)
    for i in range(6):
        g.add_vertex(i)
    
    print g.vertices
    
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)

    for vertex in g:
        for nbr in vertex.get_neighbors():
            print("(%s, %s)" % (vertex.id, nbr.id))