#!/usr/bin/python

'''
This file contains the basic implemenation of graphs. Below we explore two implementation
approaches. 

1. Adjacency Matrix
2. Adjacency Set

Ref: PluralSight, Working with Graph algorithms in Python
'''

import abc
import numpy as np 

######################################################################
# Graph is an abstract class that defines the interface for any graph 
# implmentation that we will do
######################################################################
class Graph(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacenct_vertices(self, v):
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

######################################################################
#
# Represents a graph using Adjacency matrix. A cell in the matrix has 
# a value when there exists an edge between the vertex represented by
# the row and column numbers
# Weighted graphs can hold values > 1 in the matrix cells
# A value of 0 in the cell indicates that there is not edge
#
######################################################################
class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError('Vertices', v1, 'and', v2, 'are out of bounds')

        if weight < 1:
            raise ValueError('Edge cannot have weight < 1')

        self.matrix[v1][v2] = weight
        
        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacenct_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError('Vertex', v, 'is out of bounds')

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError('Vertex', v, 'is out of bounds')

        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError('Vertices', v1, 'and', v2, 'are out of bounds')

        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacenct_vertices(i):
                print i, "-->", v


######################################################################
#
# A single node in a graph represented by an adjacency set. Every node
# has a vertex id
# Each node is associated with a set of adjacent vertices
#
######################################################################
class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError("Vertex", v, "cannot be adjacent to itself")
        self.adjacency_set.add(v)

    def get_adjacenct_vertices(self):
        return sorted(self.adjacency_set)

######################################################################
#
# Represents a graph using Adjacency sets. Every node will maintain a 
# a set which contains all it's adjacent vertices
# In the current form, this graph cannot be used to represent weighted
# edges. Only unweighted edges can be represented
#
######################################################################
class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        self.vertex_list = []

        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertex", v1, "and", v2, "are out of bounds")

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weight > 1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacenct_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex", v, "cannot be accessed")

        return self.vertex_list[v].get_adjacenct_vertices()

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex", v, "cannot be accessed")

        indegree = 0
        for vertex in self.vertex_list:
            if v in vertex.get_adjacenct_vertices():
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertex", v1, "and", v2, "are out of bounds")

        return 1

    def display(self):
        for i in self.vertex_list:
            for v in i.get_adjacenct_vertices():
                print i.vertex_id, "-->", self.vertex_list[v].vertex_id

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(5, directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)

    for i in range(4):
        print "Adjacency to:", i, g.get_adjacenct_vertices(i)

    for i in range(4):
        print "Indegree:", i, g.get_indegree(i)

    for i in range(4):
        for j in g.get_adjacenct_vertices(i):
            print "Edge weight:", i, j, "weight:", g.get_edge_weight(i, j)

    g.display()