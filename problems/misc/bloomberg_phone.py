"""

Problem Description
Implement a ride(desert,gas) method that returns true if a car can reach an oasis before it runs out of gas and false otherwise. The car can drive in four directions: top, bottom, left, right. Moving one field requires one unit of gas (used gas is an equivalent of the number of steps taken).

The desert is a 2D m x n array with five types of fields:

'c' - the starting point of the car
'o' - the oasis, our destination
'.' - sand, the car can drive through it
an integer value - a gas station, the car can refill once, as many gas units as the value indicates
'r' - a rock, cannot be crossed


Sample inputs - Expected outputs
const desert = [
    ['.','.','.','o'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','c','.','.']
];

ride(desert, 3) => false
ride(desert, 5) => true

const desertWithStation = [
    ['.','.','.','o'],
    ['.','.', 2 ,'.'],
    ['.','.','.','.'],
    ['.','c','.','.']
];

ride(desertWithStation, 3) => true
ride(desertWithStation, 5) => true

const desertWithStationAndRocks = [
    ['.','.','.','o'],
    ['.','r','r','.'],
    ['.','.','r','r'],
    ['c','.','.', 20]


    ['.','.','.','o'],
    ['.','r','r','.'],
    ['.','.','r','r'],
    ['c','.','.', 4]

    ride(desertWithStationAndRocks, 6) => True


    ['.','.','.','o'],
    ['.','r','r','.'],
    ['.','x','r','r'],
    ['c','.','.', 23]
];

ride(desertWithStationAndRocks, 2) => false
ride(desertWithStationAndRocks, 3) => true // the car visits some fields twice


"""
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def ride(desert, gas):
    for i, row in enumerate(desert):
        for j, ele in enumerate(row):
            if ele == "c":

                queue = deque([i, j, gas, set()])

                while queue:
                    curr = queue.popleft()
                    curr_i, curr_j, curr_gas = curr
                    seen.add((curr_i, curr_j))

                    if curr_gas == 0:
                        continue

                    for di, dj in directions:
                        new_i = di + curr_i
                        new_j = dj + curr_j

                        if (
                            new_i < 0
                            or new_j < 0
                            or new_i >= len(desert)
                            or new_j >= len(desert[0])
                        ):
                            continue

                        if (new_i, new_j) in seen:
                            continue

                        tile = desert[new_i][new_j]

                        if tile == "o":
                            return True

                        elif tile == "r":
                            continue

                        elif tile.isnum():
                            # start new search from cur location with gas = gas + tile
                            seen = set()
                            queue([new_i, new_j, gas + tile])

                        else:
                            queue.append([new_i, new_j, gas - 1])

                return False


"""
['x','.','.','o'],
['.','r','r','.'],
['.','.','r','r'],
['c','.','.', x4]

ride(desertWithStationAndRocks, 6) => True

memory (nm)^2





3 3 7
0 0 3



"""
