"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:
Input:
numCourses = 2, prerequisites = [[1,0]]

Output:
true

Explanation:
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.


Example 2:
Input:
numCourses = 2, prerequisites = [[1,0],[0,1]]

Output:
false

Explanation:
There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0
you should also have finished course 1. So it is impossible.
"""
from collections import defaultdict
from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Find the order of each class
        # Construct graph
        to_take = []
        top = []
        order = [0] * numCourses
        g = defaultdict(list)

        for [b, a] in prerequisites:
            """Must take a before taking b, (a -> b)"""
            order[b] += 1  # order
            g[a].append(b)  # graph

        print(f"order: {order}")
        print(f"graph: {g}")

        for i, course in enumerate(order):
            if course == 0:
                to_take.append(i)

        # while there classes to take
        while to_take:
            curr = to_take.pop(0)
            top.append(curr)

            for dep in g[curr]:
                order[dep] -= 1
                if order[dep] == 0:
                    to_take.append(dep)
        print(top)
        return numCourses == len(top)


course = Solution()
print(course.canFinish(2, [[1, 0]]))
