from random import random


class RandomizedSet:
    """
    a dict and a list

    list for easy iteration and random selection
    dict for storing pointer to list
    """

    def __init__(self):
        self.map = dict()
        self.set = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = self.length
        self.set.append(val)
        self.length += 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        temp = self.map[val]
        temp_key = self.set[self.length - 1]
        self.set[self.map[val]], self.set[self.length - 1] = (
            self.set[self.length - 1],
            self.set[self.map[val]],
        )

        self.map[temp_key] = temp
        self.set.pop()
        self.length -= 1
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return self.set[random.randint(0, self.length - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
["RandomizedSet", "insert", "insert", "remove", "insert", "remove", "getRandom"]
[[], [0], [1], [0], [2], [1], []]
