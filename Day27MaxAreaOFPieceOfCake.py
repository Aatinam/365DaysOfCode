#Day 27 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

#Problem Statement : Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake 
#to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
#Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.


class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        verticalCuts.sort()
        horizontalCuts.sort()
        verticalCuts.append(w);
        horizontalCuts.append(h);
        maxInt = (10**9)+7
        
        maxDeltaX = verticalCuts[0];
        for i in range(1, len(verticalCuts)):
            deltaX = verticalCuts[i] - verticalCuts[i-1]
            if deltaX > maxDeltaX:
                maxDeltaX = deltaX
            
        maxDeltaY = horizontalCuts[0];
        for j in range(1, len(horizontalCuts)):
            deltaY = horizontalCuts[j] - horizontalCuts[j-1];
            if deltaY > maxDeltaY:
                maxDeltaY = deltaY
            
        return (maxDeltaX*maxDeltaY)%maxInt
        