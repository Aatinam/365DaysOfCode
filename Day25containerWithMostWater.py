#Day 25 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/container-with-most-water/ 

#Problem Statement:Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
#n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, 
#together with the x-axis forms a container, such that the container contains the most water.


class Solution:
    def maxArea(self, height):
        
        maxArea = [0]* len(height)
        i = len(height) -1
        j = 0
        while (i > j):
            area = min(height[i], height[j])* (i-j)
            maxArea[i] = max(maxArea[i], area)
            maxArea[j] = max(maxArea[j], area)
            if height[j] > height[i]: # max found for height i 
                i = i-1;
                
            elif height[j] < height[i]: #max Found for height j
                j = j+1
                
            else: #one of these conditions must always be true since a number can be >, < or = any other number. 
                i = i-1
                j = j+1
                
                
        return max(maxArea)