"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key
already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this
map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the
mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
"""


class MyHashMap:
    def __init__(self):
        self.limit = 2069
        self.size = 0
        self.cap = 0.5
        self.map = [[] for _ in range(self.limit)]

    def resize(self, map):
        pass

    def put(self, key: int, value: int) -> None:
        if self.size / self.limit > self.cap:
            self.map = self.resize(self.map)

        hashed = hash(key) % self.limit
        target = self.map[hashed]

        for i, pair in enumerate(target):
            k, v = pair
            if k == key:
                target[i] = (k, value)
                return

        self.map[hashed].append((key, value))

    def get(self, key: int) -> int:
        hashed = hash(key) % self.limit
        target = self.map[hashed]

        if not target:
            return -1

        for k, v in target:
            if k == key:
                return v

        print("not found")
        return -1

    def remove(self, key: int) -> None:
        hashed = hash(key) % self.limit
        target = self.map[hashed]

        for i, pair in enumerate(target):
            k, v = pair
            if k == key:
                del target[i]
                break


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
# print(obj.map)
