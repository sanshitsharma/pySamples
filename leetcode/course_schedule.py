#!/usr/bin/env python

'''
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.

Ref: https://leetcode.com/problems/course-schedule/description/
'''

from ds.graph import AdjacencySetGraph

class Solution(object):
    def canFinish(self, num_courses, prerequisites):
        if num_courses == 0:
            return True

        # Create an adjacency set graph from the edge list
        g = AdjacencySetGraph(directed=True)
        for preReq in prerequisites:
            g.add_edge(preReq[1], preReq[0])

        #print g.display()

        # Create a precedence map which will store the indegree of each node
        precedenceMap = {}
        vertQ = []

        for v in g:
            precedenceMap[v] = g.get_indegree(v)
            if precedenceMap[v] == 0:
                vertQ.append(v)

        # Try to create a topological ordering of the nodes in the graph
        result = []
        while vertQ:
            vertex = vertQ.pop()
            result.append(vertex.id)

            for nbr in vertex.get_neighbors():
                precedenceMap[nbr] -= 1
                if precedenceMap[nbr] == 0:
                    vertQ.append(nbr)

        #print result
        return len(result) >= num_courses


if __name__ == "__main__":
    #print Solution().canFinish(2, [[1,0]])
    #print Solution().canFinish(2, [[1,0],[0,1]])
    #print Solution().canFinish(3, [[0,1], [1,2], [2,3]])