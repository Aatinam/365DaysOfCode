
#Day 24 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/robot-bounded-in-circle/

#Problem Statement : On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

#   "G": go straight 1 unit;
#   "L": turn 90 degrees to the left;
#   "R": turn 90 degrees to the right.
#   The robot performs the instructions given in order, and repeats them forever.

#Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


class Solution:
    def isRobotBounded(self, instructions):
        moves = [(-1,0), (0,-1), (1,0), (0,1)]
        # for left +1, %4 for right -1. 
        #start at -1
        currentDir = -1;
        x = 0
        y = 0
        for i in range(2*len(instructions)):
            index = i%len(instructions)
            if(instructions[index] == "G"):
                x = x+moves[currentDir][0]
                y = y+moves[currentDir][1]
                
            elif (instructions[index] == "R"):
                currentDir = (currentDir-1)%len(moves)
                
            else:
                currentDir = (currentDir+1)%len(moves)
         
        return x == 0 and y == 0 or moves[currentDir] != (0,1); #Not facing north