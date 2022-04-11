"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid
answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
course 0. So the correct course order is [0,1].


Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].


Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        q = deque()
        result = []

        # construct in-order for each class
        inOrder = [0] * numCourses
        # take a before b
        for b, a in prerequisites:
            inOrder[b] += 1
            graph[a].append(b)

        # start bfs
        for i, n in enumerate(inOrder):
            if n == 0:
                q.append(i)

        while q:
            course = q.popleft()
            result.append(course)

            for depend in graph[course]:
                inOrder[depend] -= 1
                if inOrder[depend] == 0:
                    q.append(depend)

        if len(result) != numCourses:
            """they want every class to be included, otherwise fails and return []"""
            return []

        return result

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.findOrder(*input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [2, [[1, 0]]],
    [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
    [1, [[]]],
    [3, [[1, 0], [1, 2], [0, 1]]],
]
expected = [
    [0, 1],
    [0, 1, 2, 3],
    [0],
    [],
]


sol = Solution()

sol.test(input, expected)
