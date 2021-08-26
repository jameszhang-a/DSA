"""
On an infinite plane, a robot initially stands at(0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit
"L": turn 90 degrees to the left
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0, 0) to(0, 2), turns 180 degrees, and then returns to(0, 0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or , 'R'.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """ 
            turn right by adding 1
            turn left by subtracting 1 or add 3
            mod by 4 for overflow

            assume:
            true if ending not pointing north
        """

        # 0 = North, 1 = East, 2 = South, 3 = West
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # start looking up
        idx = 0

        # starting location
        x = y = 0

        for instruction in instructions:
            if instruction == 'G':
                x += direction[idx][0]
                y += direction[idx][1]

            elif instruction == 'R':
                idx = (idx + 1) % 4

            elif instruction == "L":
                idx = (idx + 3) % 4

        # check if pointing up or at origin
        return idx != 0 or (x == 0 and y == 0)

    def isRobotBounded_2(self, instructions: str) -> bool:
        """A better solution without saving an array
        with all directions"""

        # Initialize position and velocity
        x = y = dx = 0

        # moving up
        dy = 1

        for c in instructions:
            if c == 'G':
                x += dx
                y += dy

            elif c == 'R':
                temp = dx

                dx = dy
                dy = -temp

            elif c == 'L':
                temp = dx

                dx = -dy
                dy = temp

        return (x == 0 and y == 0) or (dy != 1)
