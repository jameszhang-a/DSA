"""
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English
letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true.
Returns false if the path already exists or its parent path doesn't exist.

int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.


Example 1:
Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1

Example 2:
Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
"""
from collections import defaultdict


class Node:
    def __init__(self, val="") -> None:
        self.val = val
        self.children = defaultdict(Node)


class FileSystem:
    def __init__(self):
        self.root = Node()

    def createPath(self, path: str, value: int) -> bool:
        path = path.split("/")[1:]  # first element is useless
        node = self.root

        for i in range(len(path)):
            step = path[i]

            if step in node.children:
                node = node.children[step]
            else:
                # only add to tree if it's the last step in the paths
                if i == len(path) - 1:
                    node.children[step] = Node(value)
                    return True
                else:
                    return False

    def get(self, path: str) -> int:
        path = path.split("/")[1:]  # first element is useless
        node = self.root

        if len(path) == 1:
            if path[0] in node.children:
                return node.children[path[0]].val
            else:
                return -1

        for i in range(len(path)):
            step = path[i]

            if step in node.children and i == len(path) - 1:
                return node.children[step].val
            elif step in node.children:
                node = node.children[step]
            else:
                return -1


# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
print(obj.createPath("/leet", 1))
print(obj.createPath("/leet/code", 2))
print(obj.get("/leet/code"))
